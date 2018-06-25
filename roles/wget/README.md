wget
===+

Install and configure the `wget` command line tool.

Requirements
------------

None

Role Variables
--------------

    wget_required_packages:
      - wget

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: wget }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
