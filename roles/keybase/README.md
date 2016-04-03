hub
===

Install and configure the `keybase` command line tool.

Requirements
------------

None

Role Variables
--------------

    keybase_required_packages:
      macosx:
        - keybase

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: keybase }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
