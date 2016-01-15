ghi
===

Install and configure the `ghi` command line tool.

Requirements
------------

A working git must be present, which should be installed by the Git role dependency.

Role Variables
--------------

    ghi_token:

Dependencies
------------

Git Role

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ghi }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
