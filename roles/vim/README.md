vim
===

Install and configure the `vim` command line tool.

Requirements
------------

None

Role Variables
--------------

    vim_config_file: '{{ ansible_env.HOME }}/.vimrc'
    vim_config_directory: '{{ ansible_env.HOME }}/.vim'
    vim_config_directories:
      - after/plugin
      - autoload
      - bundle
      - colors
      - spell
      - syntax
    vim_plugins_directory: '{{ vim_config_directory }}/bundle'
    vim_packages:
      macosx:
        - vim
        - ack
        - the_silver_searcher
        - aspell
      fedora:
        - vim
        - ack
        - the_silver_searcher
        - python-flake8
        - aspell
        - aspell-en
        - ruby-devel
      ubuntu:
        - vim
        - ack-grep
        - silversearcher-ag
        - python-flake8
        - aspell
        - aspell-en
        - ruby-dev
    vim_plugins:
      - { repo: 'https://github.com/mileszs/ack.vim.git', dest: 'vim-ack' }
      - { repo: 'https://github.com/vim-airline/vim-airline.git', dest: 'vim-airline', version: '020ee382dcf960fb5f2ec2d0ad6bc64e3e1a9fe7' }
      - { repo: 'https://github.com/Townk/vim-autoclose.git', dest: 'vim-autoclose' }
      - { repo: 'https://github.com/altercation/vim-colors-solarized.git', dest: 'vim-colors-solarized' }
      - { repo: 'https://github.com/wincent/command-t.git', dest: 'vim-command-t' }
      - { repo: 'https://github.com/tpope/vim-endwise.git', dest: 'vim-endwise' }
      - { repo: 'https://github.com/nvie/vim-flake8.git', dest: 'vim-flake8' }
      - { repo: 'https://github.com/tpope/vim-fugitive.git', dest: 'vim-fugitive' }
      - { repo: 'https://github.com/scrooloose/nerdcommenter.git', dest: 'vim-nerdcommenter' }
      - { repo: 'https://github.com/scrooloose/nerdtree.git', dest: 'vim-nerdtree' }
      - { repo: 'https://github.com/ervandew/supertab.git', dest: 'vim-supertab' }
      - { repo: 'https://github.com/tpope/vim-surround.git', dest: 'vim-surround' }
      - { repo: 'https://github.com/scrooloose/syntastic.git', dest: 'vim-syntastic' }

Dependencies
------------

git, build-essentials

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: vim }

License
-------

MIT

Author Information
------------------

Christopher H. Laco <claco@chrislaco.com>
