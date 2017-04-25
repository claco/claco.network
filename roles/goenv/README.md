goenv
=====

Install and configure `goenv`.

Requirements
------------

On OSX (Darwin), a working installation of Homebrew is required.

Role Variables
--------------

    goenv_repo_url: 'https://github.com/syndbg/goenv.git'
    goenv_root_directory: '{{ ansible_env.HOME }}/.goenv'
    goenv_bin_directory: '{{ goenv_root_directory }}/bin'
    goenv_binary: '{{ goenv_bin_directory }}/goenv'
    goenv_plugins_directory: '{{ goenv_root_directory }}/plugins'
    goenv_versions_directory: '{{ goenv_root_directory }}/versions'
    goenv_plugins:
    goenv_default_packages: []

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: goenv }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
