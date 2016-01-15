git
===

Install and configure the `git` command line tool.

Requirements
------------

None

Role Variables
--------------

    git_config_directory: '{{ ansible_env.HOME }}/.gitconfig.d'
    git_config_file: '{{ ansible_env.HOME }}/.gitconfig'
    git_exludes_file: '{{ ansible_env.HOME }}/.gitexcludes'
    git_github_user:
    git_github_token:

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: git }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
