hub
===

Install and configure the `ag` command line tool.

Requirements
------------

None

Role Variables
--------------

    ag_required_packages:
      macosx:
        - the_silver_searcher
      fedora:
        - the_silver_searcher
      ubuntu:
        - silversearcher-ag

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ag }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
