#!/usr/bin/env bash

set -e

export HOMEBREW_CASK_OPTS="--appdir=/Applications --fontdir=/Library/Fonts"

sudo -v

while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &

################################################################################
# Command Line Tools
################################################################################
if ! pkgutil --pkg-info=com.apple.pkg.CLTools_Executables &> /dev/null; then
  printf "Installing Command Line Tools..."
  xcode-select --install &> /dev/null || true
  while ! pkgutil --pkg-info=com.apple.pkg.CLTools_Executables &> /dev/null; do
    sleep 10
  done
  echo "done"
else
  echo "Command Line Tools already installed...skipping"
fi

################################################################################
# Homebrew (Interactive Install)
################################################################################
if [ ! -f /usr/local/bin/brew ]; then
  echo "Installing Homebrew..."
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  brew install brew-cask
  brew cask install caskroom/fonts/font-symbola
else
  echo "Homebrew already installed...skipping"
fi

################################################################################
# Install Ansible
################################################################################
if [ ! -f /usr/local/bin/ansible-playbook ]; then
  printf "Installing Ansible..."
  brew install ansible &> /dev/null
  echo "done"
else
  echo "Ansible already installed...skipping"
fi

################################################################################
# Clone Ansible Playbooks
################################################################################
if [ ! -d ~/Projects/claco.network/.git ]; then
  printf "Cloning Playbooks..."
  mkdir -p ~/Projects/claco.network
  git clone https://github.com/claco/claco.network.git ~/Projects/claco.network
  echo "done"
else
  echo "Ansible Playbooks already installed...skipping"
fi

################################################################################
# Enable SSH Logins
################################################################################
if [[ $(sudo systemsetup -getremotelogin) = *Off* ]]; then
  printf "Enabling Remote Login..."
  sudo systemsetup -setremotelogin on
  echo "done"
else
  echo "Remote Login Enabled ...skipping"
fi

################################################################################
# Disable "Downloaded From The Internet" Open Prompts
################################################################################
printf "Disabling Internet Download Warning..."
defaults write com.apple.LaunchServices LSQuarantine -bool NO
echo "done"
echo

echo "######################################"
echo "Please reboot to have this take effect"
echo "######################################"
