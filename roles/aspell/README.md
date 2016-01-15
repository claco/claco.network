hub
===

Install and configure the `aspell` command line tool.

Requirements
------------

None

Role Variables
--------------

    aspell_required_packages:
      fedora:
        - aspell
        - aspell-en
      ubuntu:
        - aspell
        - aspell-en

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: aspell }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
