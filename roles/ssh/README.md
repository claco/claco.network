hub
===

Install and configure the `ssh` command line tool.

Requirements
------------

None

Role Variables
--------------

    ssh_keys: {}
    ssh_config_directory: '{{ ansible_env.HOME }}/.ssh'
    ssh_keys_directory: '{{ ssh_config_directory }}'
    ssh_config_file: '{{ ssh_config_directory }}/config'
    ssh_environment_file: '{{ ssh_config_directory }}/environment'
    ssh_authorized_keys_file: '{{ ssh_config_directory }}/authorized_keys'
    ssh_known_hosts_file: '{{ ssh_config_directory }}/known_hosts'
    ssh_required_packages:
      macosx:
        - ssh-copy-id
      fedora:
        - openssh
        - openssh-server
      ubuntu:
        - openssh
        - openssh-server
    ssh_known_hosts:
      - qnap.claco.network
      - gateway.claco.network
      - github.com

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ssh }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
