#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: gpg_key
author: Benjamin Woodruff
version_added: "1.6.0"
short_description: Add or remove a GnuPG key
description:
  - Add or remove a I(Gnu Privacy Guard) key, reading from a file, downloading
    from a url, or via a keyserver
notes:
  - If an C(id) value is specified, and the key already exists, it won't be
    downloaded. For performance reasons, you should always specify an C(id) with
    a C(url).
  - If a key is downloaded and doesn't match the specified C(id), it might still
    be imported. There's no easy way to check this in gpg, but it shouldn't
    matter, as simply importing a key doesn't imply any trust of that key.
options:
  state:
    description:
      - Specify if the key should be added, revoked, or re-added in the case of
        a potentially updated key. Updated keys may contain new information.
    required: no
    default: present
    choices: [present, absent, latest]
  id:
    description:
      - The key id (long or short form) or fingerprint. A long key id or full
        fingerprint is recommended, as short IDs could be subject to collision
        attacks.
    required: no
    aliases: [name]
  file:
    description:
      - A file on the remote machine to read keys from. This may contain private
        keys.
    required: no
  url:
    description:
      - A url to download the key from. This may contain private keys. Be
        careful transfering private keys over an unencrypted connection.
        Different installations of gpg may support different protocols (HTTP,
        FTP, LDAP, etc.).
    required: no
    aliases: [uri]
  keyserver:
    description:
      - When downloading using the given C(id), use a specific keyserver. If not
        provided, the system-default keyserver is used. This may be useful if
        you're running your own keyserver.
    required: no
  homedir:
    description:
      - GnuPG's home directory, containing it's configuration file. Usually this
        is C(~/.gnupg/).
    required: no
  options:
    description:
      - A configuration file on the remote machine to pass to C(gpg) using the
        C(--options) flag. Normally this is found in gpg's homedir.
    required: no
requirements: [gpg]
'''

EXAMPLES = '''
# Use a long-form key id, and pull key from the default keyserver
- gpg_key: id=2213A73C4E2569F1

# Make sure we have the latest version of a key. Updated keys can contain new
# signatures, user IDs, expiration dates, etc.
- gpg_key: id=2213A73C4E2569F1

# Pull explicitly from MIT's keyserver
- gpg_key: id=2213A73C4E2569F1 keyserver=pgp.mit.edu

# Load a key (or keys) from a file, this may contain private keys
- gpg_key: file=keyfile.gpg state=present

# Load a key from a website
- gpg_key: url='http://pgp.mit.edu/pks/lookup?op=get&search=0x2213A73C4E2569F1'
'''

def main():
    module = AnsibleModule(
        argument_spec=dict(
            state = dict(
                default = 'present',
                choices = ['present', 'absent', 'latest']
            ),
            id = dict(aliases=['name']),
            file = dict(),
            url = dict(aliases=['uri']),
            keyserver = dict(),
            homedir = dict(),
            options = dict(aliases=['config'])
        ),
        mutually_exclusive=[['file', 'url', 'keyserver']],
        required_one_of=[['id', 'file', 'url']],
        supports_check_mode=True
    )

    params = module.params
    cmd = get_gpg_cmd(module, params['homedir'], params['options'])

    if params['state'] == 'present':
        if params['id'] is not None:
            # If we know the id, we can check if the key exists locally before
            # attempting to fetch the key
            if has_key(module, cmd, params['id']):
                module.exit_json(changed=False)
            if module.check_mode:
                module.exit_json(changed=True)
        update_key(module, cmd)
    elif params['state'] == 'absent':
        del_key(module, cmd, params['id'])
    elif params['state'] == 'latest':
        update_key(module, cmd)


# Helper Functions

def get_gpg_cmd(m, homedir, options):
    '''Generate and return an array with the path to ``gpg2`` (preferred) or
    ``gpg`` (fallback), along with basic arguments that are common across
    subcommands.'''
    cmd = [m.get_bin_path('gpg', required=True)]
    if homedir is not None:
        cmd += ['--homedir', homedir]
    if options is not None:
        cmd += ['--options', options]
    if m.check_mode:
        # --dry-run is 'not completely implemented', but it works well enough
        cmd += ['--dry-run']
    return cmd

def has_key(m, cmd, key_id):
    '''Is the given ``key_id`` already in gpg's database? If someone supplies an
    id, we can avoid re-downloading it by simply checking our local database
    first.'''
    args = cmd + ['--fast-list-mode', '--list-keys', key_id]
    rc, out, err = m.run_command(args, check_rc=False)
    return rc == 0

def is_changed(stderr):
    '''Given the stderr output of gpg's execution, determine if the operation
    resulted in a changed state.'''
    return not re.search(r'^gpg:\s+unchanged:\s+[1-9]', stderr, re.MULTILINE)


# Action Functions:

def update_key(m, cmd):
    '''Given a file, url, or id-keyserver pair, attempt to import the key into
    gpg's database, updating it if it already exists.'''
    p = m.params
    if p['file'] is not None:
        import_key(m, cmd, p['file'])
    elif p['url'] is not None:
        fetch_key(m, cmd, p['url'])
    else:
        recv_key(m, cmd, p['keyserver'], p['id'])

def recv_key(m, cmd, keyserver, key_id):
    '''Download and import a key from either the default keyserver or a given
    keyserver, using it's id or fingerprint.'''
    args = list(cmd)
    if keyserver is not None:
        args += ['--keyserver', keyserver]
    args += ['--recv-keys', key_id]
    rc, out, err = m.run_command(args, check_rc=True)
    m.exit_json(changed=is_changed(err))

def import_key(m, cmd, path):
    '''Read all the keys from a file and import them.'''
    args = cmd + ['--no-tty', '--batch', '--import', path]
    rc, out, err = m.run_command(args, check_rc=False)
    m.exit_json(changed=is_changed(err))

def fetch_key(m, cmd, url):
    '''Download a key from a url/uri. Depending on installation, different
    protocols may be supported.'''
    args = cmd + ['--fetch-keys', url]
    rc, out, err = m.run_command(args, check_rc=True)
    m.exit_json(changed=is_changed(err))

def del_key(m, cmd, key_id):
    '''Causes gpg to forget about a given key.'''
    args = cmd + ['--batch', '--yes', '--delete-key', key_id]
    rc, out, err = m.run_command(args, check_rc=False)
    m.exit_json(changed=(rc == 0))

from ansible.module_utils.basic import *
main()
