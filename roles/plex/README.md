hub
===

Install and configure Plex.

Requirements
------------

None

Role Variables
--------------

    plex_required_packages:
      macosx:
        - plex-home-theater

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: plex }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
