hub
===

Install and configure the `curl` command line tool.

Requirements
------------

None

Role Variables
--------------

    curl_required_packages:
      macosx:
        - curl
      fedora:
        - curl
      ubuntu:
        - curl

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: curl }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
