hub
===

Install and configure PostgreSQL.

Requirements
------------

None

Role Variables
--------------

    postgres_required_packages:
      macosx:
        - postgres

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: postgres }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
