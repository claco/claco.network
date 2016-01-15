pyenv
=====

Install and configure `pyenv`.

Requirements
------------

On OSX (Darwin), a working installation of Homebrew is required.

Role Variables
--------------

    pyenv_repo_url: 'https://github.com/yyuu/pyenv.git'
    pyenv_root_directory: '{{ ansible_env.HOME }}/.pyenv'
    pyenv_bin_directory: '{{ pyenv_root_directory }}/bin'
    pyenv_binary: '{{ pyenv_bin_directory }}/pyenv'
    pyenv_plugins_directory: '{{ pyenv_root_directory }}/plugins'
    pyenv_versions_directory: '{{ pyenv_root_directory }}/versions'
    pyenv_plugins:
      - { repo: 'https://github.com/claco/pyenv-all', dest: 'pyenv-all' }
      - { repo: 'https://github.com/yyuu/pyenv-virtualenv.git', dest: 'pyenv-virtualenv' }
      - { repo: 'https://github.com/jawshooah/pyenv-default-packages.git', dest: 'pyenv-default-packages' }
      - { repo: 'https://github.com/yyuu/pyenv-pip-rehash.git', dest: 'pyenv-pip-rehash' }
    pyenv_default_packages: []

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: pyenv }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
