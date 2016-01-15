ruby
====

Install and configure Ruby versions using `rbenv`.

Requirements
------------

On OSX (Darwin), a working installation of Homebrew is required.

Role Variables
--------------

    ruby_default_gems: []
    ruby_install_command: 'CONFIGURE_OPTS="--disable-install-doc" {{ rbenv_bin_directory }}/rbenv install'
    ruby_versions_directory: '{{ rbenv_versions_directory }}'
    ruby_versions: []

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ruby, ruby_versions: ['1.9.3-p551', '3.4.1'] }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
