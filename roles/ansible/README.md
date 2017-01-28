hub
===

Configure and update the `ansible` command line tool.

Requirements
------------

None

Role Variables
--------------

    ansible_required_packages:
      macosx:
        - ansible
      fedora:
        - ansible
      ubuntu:
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
