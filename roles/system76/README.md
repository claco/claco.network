system76
========

Install and configure System76 additions to base operating system

Requirements
------------

None

Role Variables
--------------

    system76_repository_url: "ppa:system76-dev/stable"
    system76_required_packages:
      - "system76-driver"
    system76_desktop_background_path: "/usr/share/backgrounds"
    system76_desktop_background_uri: "file://{{ system76_desktop_background_path }}/{{ system76_desktop_background_file }}"

Dependencies
------------

None

Example Playbook
----------------

    - hosts: workstations
      roles:
         - { role: system76 } 

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
