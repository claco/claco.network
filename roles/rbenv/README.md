rbenv
=====

Install and configure `rbenv` to manage rubies built using `ruby-build`.

Requirements
------------

On OSX (Darwin), a working installation of Homebrew is required.

Role Variables
--------------

    rbenv_repo_url: 'https://github.com/rbenv/rbenv.git'
    rbenv_root_directory: '{{ ansible_env.HOME }}/.rbenv'
    rbenv_bin_directory: '{{ rbenv_root_directory }}/bin'
    rbenv_binary: '{{ rbenv_binary }}/rbenv'
    rbenv_plugins_directory: '{{ rbenv_root_directory }}/plugins'
    rbenv_versions_directory: '{{ rbenv_root_directory }}/versions'
    rbenv_plugins:
      - { repo: 'https://github.com/rbenv/ruby-build.git', dest: 'ruby-build' }
      - { repo: 'https://github.com/ConradIrwin/rbenv-all', dest: 'rbenv-all' }
      - { repo: 'https://github.com/sstephenson/rbenv-default-gems.git', dest: 'rbenv-default-gems' }
      - { repo: 'https://github.com/sstephenson/rbenv-gem-rehash.git', dest: 'rbenv-gem-rehash' }
      - { repo: 'https://github.com/nicknovitski/rbenv-gem-update', dest: 'rbenv-gem-update' }
      - { repo: 'https://github.com/tpope/rbenv-readline.git', dest: 'rbenv-readline' }
    rbenv_default_gems: []

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: rbenv }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
