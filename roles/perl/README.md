perl
====

Install and configure Perl versions using `plenv`.

Requirements
------------

On OSX (Darwin), a working installation of Homebrew is required.

Role Variables
--------------

    perl_install_command: '{{ plenv_bin_directory }}/plenv install'
    perl_versions_directory: '{{ plenv_versions_directory }}'
    perl_versions: []

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: perl, perl_versions: ['5.20.3', '5.22.1'] }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
