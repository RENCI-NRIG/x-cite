# Linux, Commandline, and Scripting

## Some words about Linux


## Some words about command line




## The shell

A shell is an interactive program that accepts commands and passes
those commands to the operating systems to execute.

In the shell, you type a command, hit enter, and the command gets
executed.  Shell is the program that is responsible for accepting your
commands, executing them, and printing the results on a console.

The screenshot below shows a how this works in practice: using a
terminal program, I'm using `ssh` command to access the host
`lnx201.classe.cornell.edu` (just `lnx201` henceforth), and then I'm
running some commands on `lnx201`.

![shell screenshot](./lnx201.png)

Nearly all Linux distributions ship a shell named `bash`.  In the
`lnx201` environment that you access, `bash` is the default shell. You
will be staring at a bash prompt when you ssh to `lnx201`.

Although `bash` is the most popular shell, many other shells exist
too: `csh`, `ksh`, `dash`, `zsh`, and so on.  But let us not get
distracted and just commit to `bash` for now.


## Useful shell builtins

TODO: probably don't have to talk about this now?


## Directory navigation

Linux organizes directories and files in a /hierarchical directory
structure/, meaning, they are organized in a tree-like pattern of
directories.

The first, or top-level directory of this tree is called the "root
directory", or "/".


- files, directories

## Directory structure

- /bin, /sbin, /tmp, /var, /etc, /home, /dev etc.


## The current working directory

At any time in the shell, we are "inside" a single directory, known as
the current working directory.  When you list files with `ls`, a list
of files and directories of the current working directory will be
printed on the output.

When you log in to `lnx201`, initially you will be in a directory
named `/home/${USER}`, where `${USER}` is your username on `lnx201`.
This is what is known as your /home directory/.  When you log in
first, your home directory will be your current working directory. 

To find where you are, use the command `pwd`.

The below commands are useful:

- `mkdir test` will create a directory named `test`
- `cd test` will change the working directory to `test`.
- `ls` will list files and directories in the current working
  directory.

`cd -` is useful: it will switch you to the directory that you were
  previously in.
  
`.` and `..` are special directory names: `.` means the current
directory, and `..` means its parent directory, or the directory above
it in the directory hierarchy.
 
- directory navigation: ls, cd, mkdir, rm, ln, pwd, touch


## Permissions and ownership

- chmod, chown


## Pipes, job control

- pipes
- redirection (> and <)
- background and foreground processes
- listing processes (ps, top, htop)
- signals
- terminating processes (kill)


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
