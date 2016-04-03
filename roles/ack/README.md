hub
===

Install and configure the `ack` command line tool.

Requirements
------------

None

Role Variables
--------------

    ack_required_packages:
      macosx:
        - ack
      fedora:
        - ack
      ubuntu:
        - ack-grep

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ack }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
