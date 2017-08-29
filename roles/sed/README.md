hub
===

Install and configure the `sed` command line tool.

Requirements
------------

None

Role Variables
--------------

    sed_required_packages:
      macosx:
        - gnu-sed

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: sed }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
