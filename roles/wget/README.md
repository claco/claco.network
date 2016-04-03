hub
===

Install and configure the `wget` command line tool.

Requirements
------------

None

Role Variables
--------------

    wget_required_packages:
      macosx:
        - wget
      fedora:
        - wget
      ubuntu:
        - wget

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: curl }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
