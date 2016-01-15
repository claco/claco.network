plenv
=====

Install and configure `plenv`.

Requirements
------------

Requires a working git install.

Role Variables
--------------

    plenv_repo_url: 'https://github.com/tokuhirom/plenv.git'
    plenv_root_directory: '{{ ansible_env.HOME }}/.plenv'
    plenv_bin_directory: '{{ plenv_root_directory }}/bin'
    plenv_binary: '{{ plenv_bin_directory }}/plenv'
    plenv_plugins_directory: '{{ plenv_root_directory }}/plugins'
    plenv_versions_directory: '{{ plenv_root_directory }}/versions'
    plenv_plugins:
      - { repo: 'https://github.com/tokuhirom/Perl-Build.git', dest: 'perl-build' }
      - { repo: 'https://github.com/claco/plenv-all', dest: 'plenv-all' }

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: plenv }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
