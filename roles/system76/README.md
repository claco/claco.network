hub
===

Install and configure the System76 drivers

Requirements
------------

None

Role Variables
--------------

    system76_required_packages:
      ubuntu:
        - system76-driver

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: system76 } 

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
