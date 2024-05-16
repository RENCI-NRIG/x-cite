---
title: "The commmand-line"
subtitle: "X-CITE 2024 workshop"
# author: "Sajith Sasidharan"
date: last-modified
format:
  revealjs:
    theme: default
    output-file: commandline-slides-revealjs.html
    footer: |
      <https://xcitecourse.org/>

      Supported by the NSF awards
      [OAC-2320373](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2320373),
      [OAC-2320374](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2320374),
      and
      [OAC-2320375](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2320375).

    logo: ../../images/x-cite-logo-2.png
  beamer:
    # aspectratio: 32
    # navigation: horizontal
    theme: default
    logo: ../../images/x-cite-logo-2.png
---

# Preliminaries

Getting into CLASSE Linux systems

## Assumptions

- You have your CLASSE accounts set up.
  - Talk to CLASSE staff otherwise!

- Options:

  - Use ssh
  - Use NoMachine
  - Use JupyterLab


## Use SSH

![](lnx201.png)

`ssh ${username}@lnx201.classe.cornell.edu`


## Use NoMachine

![](nomachine.png)

<https://wiki.classe.cornell.edu/Computing/NoMachine>


## Use JupyterLab

![](jupyter01.png)

<https://jupyter01.classe.cornell.edu/>


# Linux, command line, etc.

## Linux

- A fairly popular operating system.
  - (Actually an OS kernel, plus userland from various other projects.
    But those are details...)
- Unix-like, which traces back to 1969, therefore has accumulated
  quirks.
  - Expect "hysterical raisins".

## `lnx201`

- The Linux host we'll be using is `lnx201.classe.cornell.edu`.
- Runs a _distribution_ called Scientific Linux.
- Good enough for general use.
- Do not run anything resource heavy on `lnx201`.


## The command line

![](lnx201.png)

- You will type _commands_ in a _shell_ (text user interface), hint
  {{<kbd enter>}} key, and then things happen.

- (As opposed to clicking on GUI widgets.)

## Commands

- Commands are either programs or shell builtins.
- Use one of these commands to get some documentation:

  - `man ${command}`
  - `info ${command}`
  - or `${command} --help` (sometimes!)

## The shell

- A program that accepts commands 
- Shell passes commands to the OS to execute
- A popular shell is `bash`, which is the default on `lnx201`.


## Bash

- "Bourne-again shell" 
  - (Based on the earlier Bourne shell)
  - from the [GNU project][gnu]
  - `/bin/bash` is the program
- For documentation: `info bash` or `man bash`.

[gnu]: http://gnu.org/


## Environment variables

# Files and directories

## Directory navigation

## Wildcards

## The current working directory

## Fun facts about file names

## Standard input, output, and error

## I/O redirection

## Pipes

## Symbolic links

# Users and Groups

## Permissions and ownership

## Changing permissions


# Processes

## Background and foreground processes

## Terminating processes

## Signals

# Shell Scripting

# Other tools of the trade

## Text editors

Many choices! Use:

- Emacs
- Vim
- Nano
- JupyterLab


## Terminal multiplexers

![](tmux.png)
