# Linux, Commandline, and Scripting

## Some words about Linux


## Some words about command line




## The shell

The shell is an interactive program that accepts keyboard commands and
passes those commands to the operating systems to execute.  

You type a command, hit enter, and the command gets executed.  Shell
is the program that is responsible for accepting your commands,
executing them, and printing the results on a console, as you see in
the screenshot below:

![a shell session](./lnx201.png)

Nearly all Linux distributions ship a shell named `bash`.  Although
`bash` is likely the most popular shell, many other shells exist too:
`csh`, `ksh`, `dash`, `zsh`, and so on.  But let us not get distracted
and just commit to `bash` for now.

In the lnx201 environment that you access, `bash` is the default
shell. You will be staring at a bash prompt when you ssh to lnx201.


## Useful shell builtins

TODO: probably don't have to talk about this now?


## Directory navigation

- files, directories
- directory navigation: ls, cd, mkdir, rm, ln
- permissions, ownership
- chmod, chown
- directory structure (/bin, /sbin, /tmp, /var, /etc, /home, /dev)


## Pipes, job control

- pipes
- redirection (> and <)
- background and foreground processes
- listing processes
- signals
- terminating processes


## Environment variables

- What are they?
- How to use them?


## Basic UNIX tools

- echo

- cat
- tail

- head
- tail

- sed
- awk
- grep
- sleep

- ping
- netstat

- ifconfig
- ip

- ps
- top
- htop
- kill
- killall

- hostname
- uname


- date
- cal

- clear
- history

- ssh
- scp
- sftp
- ftp
- wget
- curl

- ?

## Aliases


## Dotfiles


## Editors


## Writing shell scripts

- shebangs
- functions
- making files executable
- ~/.local/bin maybe?


## Nifty: terminal multiplexers


## Finding help and documentation

- finding help: man, info, the web


## Further reading

- https://missing.csail.mit.edu/2020/shell-tools/
