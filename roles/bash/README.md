bash
====

Install and configure the `bash` shell.

Requirements
------------

None

Role Variables
--------------

    bash_profile_file: '{{ ansible_env.HOME }}/.bash_profile'
    bash_rc_file: '{{ ansible_env.HOME }}/.bashrc'
    bash_inputrc_file: '{{ ansible_env.HOME }}/.inputrc'
    bash_logout_file: '{{ ansible_env.HOME }}/.bash_logout'
    bash_completion_directory: '{{ ansible_env.HOME }}/.bash_completion.d'
    bash_profile_directory: '{{ ansible_env.HOME }}/.bash_profile.d'
    bash_required_packages:
      macosx:
        - bash
        - bash-completion
      fedora:
        - bash
        - bash-completion
      ubuntu:
        - bash
        - bash-completion

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: bash }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
