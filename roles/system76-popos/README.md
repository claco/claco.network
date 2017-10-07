system76-popos
==============

Install and configure System76 Pop!_OS

Requirements
------------

None

Role Variables
--------------

    system76_popos_repository_url: "ppa:system76/pop"
    system76_popos_required_packages:
      - "pop-theme"
    system76_popos_desktop_background_path: "/usr/share/backgrounds"
    system76_popos_desktop_background_uri: "file://{{ system76_popos_desktop_background_path }}/{{ system76_popos_desktop_background_file }}"

Dependencies
------------

None

Example Playbook
----------------

    - hosts: workstations
      roles:
         - { role: system76-popos } 

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
