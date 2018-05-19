ansible
=======

Configure and update the `ansible` command line tool.

Requirements
------------

None

Role Variables
--------------

    ansible_required_packages:
      - ansible

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansible }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
