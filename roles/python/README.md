python
======

Install and configure Python versions using `pyenv`.

Requirements
------------

On OSX (Darwin), a working installation of Homebrew is required.

Role Variables
--------------

    python_install_command: '{{ pyenv_bin_directory }}/pyenv install'
    python_versions_diectory: '{{ pyenv_versions_directory }}'
    python_versions: []

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: python, python_versions: ['2.7.10', '3.4.1'] }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
