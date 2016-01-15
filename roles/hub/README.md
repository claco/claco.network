hub
===

Install and configure the `hub` command line tool.

Requirements
------------

A working git must be present, which should be installed by the Git role dependency.

Role Variables
--------------

None

Dependencies
------------

Git Role

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: hub }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
