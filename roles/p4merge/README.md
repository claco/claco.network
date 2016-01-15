p4merge
=======

Install and configure the `p4merge` command line tool.

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
         - { role: p4merge }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
