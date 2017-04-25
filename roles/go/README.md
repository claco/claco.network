go
==

Install and configure Go versions using `goenv`.

Requirements
------------

On OSX (Darwin), a working installation of Homebrew is required.

Role Variables
--------------

    go_install_command: '{{ goenv_bin_directory }}/goenv install'
    go_versions_diectory: '{{ goenv_versions_directory }}'
    go_versions: []

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: go, go_versions: ['1.7', '1.8'] }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
