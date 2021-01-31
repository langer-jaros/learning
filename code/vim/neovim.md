# Neovim

Neovim - a Vim taken a step further.

`2021 Jan 31, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [Introduction](#introduction)
* [Installation](#installation)
    * [Install neovim](#install-neovim)
    * [Create config file](#create-config-file)
    * [Create space for plugins](#create-space-for-plugins)
    * [Install vim-plug plugin manager](#install-vim-plug-plugin-manager)
    * [Plugins](#plugins)
        * [neoclide/coc.nvim](#neoclidecocnvim)
        * [morhetz/gruvbox](#morhetzgruvbox)
    * [Modify the config file](#modify-the-config-file)
    * [How to Configure Vim like VSCode (benawad)](#how-to-configure-vim-like-vscode-benawad)

<!-- /TOC -->

## Introduction

- [Meet Neovim (vimcasts.org)](http://vimcasts.org/episodes/meet-neovim/)

## Installation

### Install neovim

```sh
sudo add-apt-repository ppa:neovim-ppa/stable       # version 0.4.4
# sudo add-apt-repository ppa:neovim-ppa/unstable   # version 0.5.0-dev
sudo apt-get update
sudo apt-get install neovim
```

- [Install neovim ubuntu/linux mint](https://vi.stackexchange.com/questions/25192/how-to-install-stable-version-of-neovim-on-ubuntu-18-04)

### Create config file

```sh
# Do this only if the file does not exist already!
mkdir -p ~/.config/nvim
echo "\
set tabstop=4
set softtabstop=0
set expandtab
set shiftwidth=4
set smarttab
set list
" > ~/.config/nvim/init.vim
```

### Create space for plugins

```sh
mkdir -p ~/.vim/plugins
```

### Install vim-plug plugin manager

```sh
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

- [Install vim-plugin manager](https://www.linode.com/docs/guides/how-to-install-neovim-and-plugins-with-vim-plug/)

### Plugins

#### [neoclide/coc.nvim](https://github.com/neoclide/coc.nvim)

Install nodejs >= 10.12:

```sh
curl -sL install-node.now.sh/lts | bash
```

#### [morhetz/gruvbox](https://github.com/morhetz/gruvbox)

### Modify the config file

Usually this is the very first lines of the init.vim file.

```init.vim
call plug#begin('~/.vim/plugins')

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'morhetz/gruvbox'

call plug#end()
```

Restart nvim and run `:PlugInstall`.

### [How to Configure Vim like VSCode (benawad)](https://www.youtube.com/watch?v=gnupOrSEikQ)

- [init.vim file from Ben Awad](https://gist.github.com/benawad/b768f5a5bbd92c8baabd363b7e79786f)

<!--
```sh
echo "\
\" Use release branch (recommend)
Plug 'neoclide/coc.nvim', {'branch': 'release'}
" | cat - ~/.config/nvim/init.vim > tmp && mv tmp ~/.config/nvim/init.vim
```
-->
