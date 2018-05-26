curl
===+

Install and configure the `curl` command line tool.

Requirements
------------

None

Role Variables
--------------

    curl_required_packages:
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
