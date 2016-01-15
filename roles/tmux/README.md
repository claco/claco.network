hub
===

Install and configure the `tmux` command line tool.

Requirements
------------

None

Role Variables
--------------

    tmux_config_file: '{{ ansible_env.HOME }}/.tmux.conf'

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: tmux }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
