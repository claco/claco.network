gist
====

Install and configure the `gist` command line tool.

Requirements
------------

A working git must be present, which should be installed by the Git role dependency.

Role Variables
--------------

    gist_token:

Dependencies
------------

Git Role

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: gist }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
