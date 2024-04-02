# Linux, Commandline, and Scripting

The following notes assume that you are all set up to use your
accounts on the CLASSE Linux systems.  You know how to use `ssh` to
access those machines, and you might know enough commands to find your
way around, depending on your level of familiarity with these systems.

But it probably is not a good idea to assume that you know your way
around, so let us see what you might need to know to be a fairly
effective user of the systems.


## Some words about Linux


## Some words about command line

Suppose you want to find all the text files in a directory that
contain a certain pattern, like "hello".  How would you do that?

Now suppose you want to replace all instances of "hello" with
"bonjour". How would you do that?

You can do these things using the Linux command line.  You would be
invoking commands like `find` and `grep` and `sed` and `awk`, instead
of using programs with a graphical user interfaces.

Plenty of software with friendly user interfaces exist, and they are
often easier to use.  In order to use the command line, you will have
to be familiar with often arcane tools and memorize stuff.

Why would you want to use the command line then?

Because, for certain types of tasks, it is often quick and efficient
to use the command line.  You can "chain" or compose separate programs
that do different things together.  You can also save fairly
complicated tasks in the form of scripts for later use, and share them
with your colleagues.

Learning to use the command line well will leave more power on your
hands.


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


# Directory navigation

Linux organizes directories and files in a _hierarchical directory
structure_, meaning, they are organized in a tree-like pattern.


- TODO: files, directories

## Directory structure

The first, or top-level directory of this tree is a special directory,
called the "root directory", or `/`.  All other directories are under
the root directory.  You can list things under `/` with the command
`ls /`:

```console
[user@lnx201 ~]$ ls /
bin   cdat  cvmfs  etc   lib    media  mnt  nfs   opt   root  sbin  sys  usr
boot  cifs  dev    home  lib64  misc   net  null  proc  run   srv   tmp  var
```

It is useful to know about some of these directories:

- `home` is where user home directories are.
  - `root` is the home directory for `root` user, aka superuser.
- `bin` and `sbib` are for programs.
- `lib` and `lib64` are for libraries.
- `etc` is for configuration files.
- `tmp` is for temporary files
- `proc` provides an interface with processes.


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
- `rm` will remove a file.
- `rm <name of directory>` will _not_ remove a directory; you have to
  remove it _recursively_, like so: `rm -r <name of directory>`.
  

`cd -` is useful: it will switch you to the directory that you were
  previously in.
  
`.` and `..` are special directory names: `.` means the current
directory, and `..` means its parent directory, or the directory above
it in the directory hierarchy.
 
`touch` command is used to change file timestamps.  You can also use
`touch` to create an empty file, like so: `touch test.txt`.

- TODO: directory navigation: ls, cd, mkdir, rm, ln, pwd, touch


## Users and groups

Linux is a multi-user operating system.  Since many people can be
using the system, there needs to be mechanisms in place to ensure
separation between them, while ensuring that they can access shared
resources when necessary.

The basic mechanism is the concept of users and groups.

The root user is a special user that has all the permissions. They can
change most things about the system.  The root user can change system
configuration, add and remove users and groups, etc.

Most of the time, we do not need neither the power nor the
responsibilities of the root user.  So we have a non-root, _regular_
user account in `lnx201`.

Your account also belongs to certain _groups_. Groups are the way to
grant permission to a group of accounts.  You can find the groups you
belong to using `groups` command:

```console
[ssasidharan@lnx201 ~]$ groups 
chess classeuser
[ssasidharan@lnx201 ~]$ 
```

Users and groups have distinct numerical identifiers too.  You can
find them with `id` command:

```console
[ssasidharan@lnx201 ~]$ id
uid=63499(ssasidharan) gid=262(chess) groups=262(chess),750(classeuser)
```

If you run `ls -l` (`-l` is for long listing format) command to list
files and folders in your home directory, the result will be something
like this:

```console
[ssasidharan@lnx201 ~]$ ls -l
total 4
drwxr-xr-x 2 ssasidharan chess   28 Mar 28 09:36 bin
drwxr-xr-x 2 ssasidharan chess  144 Mar 12 00:27 CLASSE_shortcuts
drwxr-xr-x 2 ssasidharan chess   30 Mar 26 15:22 Desktop
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Documents
lrwxrwxrwx 1 ssasidharan chess   31 Mar 26 15:21 Downloads -> /cdat/tem/ssasidharan/Downloads
-rw-r--r-- 1 ssasidharan chess 3254 Mar  7 15:55 helloworld.ipynb
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Music
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Pictures
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Public
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Templates
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Videos
```

Let us see what the above columns means:

- The first column lists permissions on the file/folder.  (We will see
  what this means in the next section.)
- The second column shows number of links to it.
- The third one shows the user who owns it.
- The fourth one shows the group that owns the file.
- The fifth one is the size of the file in bytes.  Note that
directories are a little special here -- what you see here is not the
total size of all the files and folders under the directory, but the
space the directory itself uses on disk.
- The next column (the whole `Mar 26 15:21` segment) shows a timestamp
  when the file/folder was last modified.
- Finally, the name of the file/folder.  Note that `Downloads ->
  /cdat/tem/ssasidharan/Downloads` is a bit special: it means that
  `Downloads` folder is in fact a link to
  `/cdat/tem/ssasidharan/Downloads`.


## Permissions and ownership

Let us see what a string like `drwxr-xr-x` from the above example
means.  This string, sometimes called "permission bits" or "file mode
bits", is ten characters long.  Each of the characters are shorthand
signifying something.

- The first `d` stands for `directory`.  (For files, this will be a `-`.)
- The next three `rwx` are for user's permissions.
- The next three `r-x` are for group permissions.
- The final three `r-x` are for permissions for the rest of the users.

Now, what do those `r` and `w` and `x` mean?

- `r` means permission to **r**ead.
- `w` means permission to **w**rite.
- `x` means permission to e**x**ecute, in the case of files.  In the
  case of directories, `x` means that you can `cd` into them.

### Changing permissions with `chmod`

You can use `chmod` command to change permissions.  If you create a
shell script named `test.sh`, for example, it won't be executable by
default.  You will have to change the file mode bits using `chmod`:

```console
[ssasidharan@lnx201 ~]$ ls -l test.sh 
-rw-r--r-- 1 ssasidharan chess 0 Mar 28 13:39 test.sh
[ssasidharan@lnx201 ~]$ ./test.sh
-bash: ./test.sh: Permission denied
[ssasidharan@lnx201 ~]$ chmod +x test.sh 
[ssasidharan@lnx201 ~]$ ls -l test.sh 
-rwxr-xr-x 1 ssasidharan chess 0 Mar 28 13:39 test.sh
[ssasidharan@lnx201 ~]$ ./test.sh
```

You can remove the `x` bit like so:

```
[ssasidharan@lnx201 ~]$ chmod -x test.sh
[ssasidharan@lnx201 ~]$ ls -l test.sh 
-rw-r--r-- 1 ssasidharan chess 0 Mar 28 13:39 test.sh
```

You can also grant permission to just the **o**wner, or **g**roup, or others:

```console
[ssasidharan@lnx201 ~]$ chmod u+x test.sh 
[ssasidharan@lnx201 ~]$ ls -l test.sh 
-rwxr--r-- 1 ssasidharan chess 0 Mar 28 13:39 test.sh
[ssasidharan@lnx201 ~]$ chmod g+x test.sh 
[ssasidharan@lnx201 ~]$ ls -l test.sh 
-rwxr-xr-- 1 ssasidharan chess 0 Mar 28 13:39 test.sh
[ssasidharan@lnx201 ~]$ chmod o+x test.sh 
[ssasidharan@lnx201 ~]$ ls -l test.sh 
-rwxr-xr-x 1 ssasidharan chess 0 Mar 28 13:39 test.sh
```

You can also combine `u`, `g`, `o` bits and `r`, `w`, `x` bits with
`+` or `-`:

```console
[ssasidharan@lnx201 ~]$ chmod ugo-r test.sh 
[ssasidharan@lnx201 ~]$ ls -l test.sh 
--wx--x--x 1 ssasidharan chess 0 Mar 28 13:39 test.sh
```

I just made the file unreadable by everyone, even me!

```console
[ssasidharan@lnx201 ~]$ cat test.sh 
cat: test.sh: Permission denied
```

Of course you can restore the permission with `chmod ugo+r test.sh` 

Note that when invoking `chmod`, `a` (or **a**ll) is equivalent of
`ugo` (user + group + others).  You can also omit `a` or `ugo` if you
want everyone to have the same permissions.  So the below all are
equivalent:

```console
[ssasidharan@lnx201 ~]$ chmod ugo+r test.sh
[ssasidharan@lnx201 ~]$ chmod a+r test.sh
[ssasidharan@lnx201 ~]$ chmod +r test.sh
```

(If you want to change owner or group of a file/folder, you can do
that with `chown` and `chgrp`.  This probably is not immediately
useful; it is enough to know that these commands exist.)


## Symbolic links

TODO

## Noteworthy facts about file names

- File/folder names that begin with a `.` (period character) are
  "hidden": meaning that they will not be listed in the output of `ls`
  command by default.  You can list them with `ls -a`. They are also
  called _dotfiles_.
  
  Configuration files for the programs you use (such as `.bashrc` for
  bash configuration) are often saved in hidden files.  This way they
  usually stay out of your way without creating a clutter.
  
- File/folder names and commands are case sensitive in Linux.  Thus
  `Notes.txt` and `notes.txt` and `NOTES.TXT` are all distinct files.

- As a matter of convenience, it is better to avoid spaces and special
  characters in file/folder names, as it will make tasks a little more
  difficult. If you need to represent spaces between words, you can
  replace spaces with `_` (the underscore character).


# Standard input, output, and error

Nearly all programs produce output of some kind, and quite often they
also accept input.

Following the Unix tradition of "everything is a file", programs send
their output to special files called _standard output_ or _standard
error_`, and they read input from _standard input_.  They are also
known as `stdout`, `stderr`, and `stdin`, respectively.


## I/O redirection

I/O redirection lets us to change where standard output gets printed.
To redirect standard output, we use the `>` operator.

```console
[ssasidharan@lnx201 ~]$ ls -l > ls-output.txt
```

As a result of redirection, a new file named `ls-output.txt` will be
created.  You can view its contents using `cat` command.

```console
[ssasidharan@lnx201 ~]$ ls -l ls-output.txt 
-rw-r--r-- 1 ssasidharan chess 807 Apr  1 17:32 ls-output.txt
[ssasidharan@lnx201 ~]$ cat ls-output.txt 
total 4
drwxr-xr-x 2 ssasidharan chess   28 Mar 28 09:36 bin
drwxr-xr-x 2 ssasidharan chess  144 Mar 12 00:27 CLASSE_shortcuts
drwxr-xr-x 2 ssasidharan chess   30 Mar 26 15:22 Desktop
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Documents
lrwxrwxrwx 1 ssasidharan chess   31 Mar 26 15:21 Downloads -> /cdat/tem/ssasidharan/Downloads
-rw-r--r-- 1 ssasidharan chess 3254 Mar  7 15:55 helloworld.ipynb
-rw-r--r-- 1 ssasidharan chess    0 Apr  1 17:32 ls-output.txt
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Music
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Pictures
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Public
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Templates
-rwxr-xr-x 1 ssasidharan chess    0 Mar 28 13:39 test.sh
drwxr-xr-x 2 ssasidharan chess    6 Mar 26 15:21 Videos
```

Note that if there already was a file named `ls-output.txt`, the
redirection above would have overwritten its contents.  You want to be
careful about this.

What if you want to discard `stdout` completely?  You can redirect it
to the special file `/dev/null`:

```console
[ssasidharan@lnx201 ~]$ ls -l >> ls-output.txt
```

If you want to append `stdout` to a file instead of overwriting it,
you can use `>>` operator:

```console
[ssasidharan@lnx201 ~]$ ls -l >> ls-output.txt
```

The  `<` operator is a sort of inverse of the `>` operator:

```console
[ssasidharan@lnx201 ~]$ echo "Shall I compare thee to a summer’s day?" > sonnet18.txt
[ssasidharan@lnx201 ~]$ cat sonnet18.txt 
Shall I compare thee to a summer’s day?
[ssasidharan@lnx201 ~]$ cat < sonnet18.txt 
Shall I compare thee to a summer’s day?
```

(TODO: explain the above: `echo` and the different usage of `cat`.)


## Pipes

Programs can write to standard output.  Programs can also read from
standard input. This means we can "chain" them together, such that one
programs standard output is "piped" into another program's standard
input.

The operator to do this is `|` (vertical bar), also known as a pipe,
and it is used in this manner: `command1 | command2`.


```console
[ssasidharan@lnx201 ~]$ ls -l /bin/ | less
```

The output of `ls -l /bin` is fairly large, so we pipe it into `less`,
which allows you to scroll the output backward and forward, using _up_
and _down_ keyboard keys.

You can form longer pipes like this:

``` console
[ssasidharan@lnx201 ~]$ ls /bin /usr/bin /sbin /usr/sbin | sort | uniq | wc
   4289    4288   46820
```

- `sort` will sort lines of text files.
- `uniq` is used to filter adjacent matching lines the output of
  `sort`.
- `wc` is a **w**ord **c**ount program.  It counts lines, words, and
  bytes present in its input.


## Controlling processes

When you run a command, it results in what is called a _process_.
Processes are running instances of programs which use CPU, memory, and
possibly other resources.

### Listing processes

You can list running processes using `ps` command:

```console
[ssasidharan@lnx201 ~]$ ps
    PID TTY          TIME CMD
 694411 pts/81   00:00:00 ps
3479688 pts/81   00:00:00 bash
```

By default, `ps` prints processes of the current user and terminal in
four columns:

- `PID` is process id.
- `TTY` is the terminal associated with the process.
- `TIME` is the elapsed CPU time for the process.
- `CMD` is the command that created the process.

Usually there are many more processes running in the system, and
sometimes they were started by other users.  You can list them, with
more detail, by passing some options to `ps`:

```console
[ssasidharan@lnx201 ~]$ ps -ef | head
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 Jan10 ?        03:14:05 /usr/lib/systemd/systemd --switched-root --system --deserialize 22
root           2       0  0 Jan10 ?        00:01:12 [kthreadd]
root           6       2  0 Jan10 ?        00:12:16 [ksoftirqd/0]
root           7       2  0 Jan10 ?        00:01:10 [migration/0]
root           8       2  0 Jan10 ?        00:00:00 [rcu_bh]
root           9       2  0 Jan10 ?        11:14:26 [rcu_sched]
root          10       2  0 Jan10 ?        00:00:00 [lru-add-drain]
root          11       2  0 Jan10 ?        00:05:22 [watchdog/0]
root          12       2  0 Jan10 ?        00:00:24 [watchdog/1]
```

Run `man ps` for details.

Programs like `top` and `htop` will list processes in friendlier,
fancier format.


### Background and foreground processes

By default, commands run in the _foreground_: they do their thing, use
the terminal (to read input, print output), and finally exit.  You
need to wait for a foreground process to end before you start the next
one, or use another terminal.

When have a long-running process, you have the option of sending it to
the _background_, using the `&` operator:

```console
[ssasidharan@lnx201 ~]$ sleep 100 &
[1] 949751
```

You can use `Control + Z` to stop a foreground process and send it to
the background:

```
[ssasidharan@lnx201 ~]$ sleep 100
^Z
[1]+  Stopped                 sleep 100
```

You can list background processes using `jobs` command:

```console
[ssasidharan@lnx201 ~]$ jobs
[1]-  Running                 sleep 100 &
[2]+  Stopped                 sleep 100
```

You can bring a background process to foreground using `fg` command,
and you can terminate it using `Control + C`:

```console
[ssasidharan@lnx201 ~]$ fg 2
sleep 100
^C
[ssasidharan@lnx201 ~]$ 
```

You can use `bg` command to resume a stopped background process:

```console
[ssasidharan@lnx201 ~]$ sleep 100 &
[1] 1746205
[ssasidharan@lnx201 ~]$ sleep 100 
^Z
[2]+  Stopped                 sleep 100
[ssasidharan@lnx201 ~]$ jobs
[1]-  Running                 sleep 100 &
[2]+  Stopped                 sleep 100
[ssasidharan@lnx201 ~]$ bg %2
[2]+ sleep 100 &
```

### Terminating processes

Sometimes you might want to terminate a program, perhaps because it is
using too much CPU or memory. You can find out the offending program's
ID using `ps` or `top` or `htop`, and then you can use `kill` command
to end the process.

By default, `kill` sends a signal called `SIGTERM` (more on signals
later).  If `SIGTERM` is unable to terminate the process (such as when
the program is ignoring `SIGTERM`), you can try `SIGKILL`:

```console
[ssasidharan@lnx201 ~]$ ps
    PID TTY          TIME CMD
 796679 pts/116  00:00:00 bash
1185454 pts/116  00:00:00 ps
1748299 pts/116  00:00:00 sleep
[ssasidharan@lnx201 ~]$ kill 1748299
[ssasidharan@lnx201 ~]$ ps
    PID TTY          TIME CMD
 796679 pts/116  00:00:00 bash
1203470 pts/116  00:00:00 ps
1748299 pts/116  00:00:00 sleep
[ssasidharan@lnx201 ~]$ kill -SIGKILL 1748299
[2]+  Killed                  sleep 100
```

You can use `killall` command to kill processes by name:

```console
[ssasidharan@lnx201 ~]$ killall sleep
sleep(1469283): Operation not permitted
sleep(1509215): Operation not permitted
sleep: no process found
```

In the above example, you are not running a `sleep` process, but some
other users are, but you are not allowed to terminate them.


### Signals

As mentioned above, `kill` command sends _signals_ to running
processes, and we've already seen `SIGTERM` and `SIGKILL`.  Signals
are a process control mechanism. They are used to stop, resume, or
terminate processes, and more.

When we use `Control + C` or `Control + Z`, we are sending signals to
process -- `SIGINT` (or "keyboard interrupt") and `SIGTSTP` (or
"terminal stop"), respectively.

Signals have numbers: `SIGKILL` is 9, so you can use `kill -9 <pid>`
instead of `kill -SIGKILL <pid>`.  You can also omit the `SIG` prefix,
and use `kill -KILL <pid>`.

Here are some common signals:

<!-- TODO: edit below; copy-pasted from `man 7 signal` -->

```
       Signal     Value     Action   Comment
       ──────────────────────────────────────────────────────────────────────
       SIGHUP        1       Term    Hangup detected on controlling terminal
                                     or death of controlling process
       SIGINT        2       Term    Interrupt from keyboard
       SIGQUIT       3       Core    Quit from keyboard
       SIGILL        4       Core    Illegal Instruction
       SIGABRT       6       Core    Abort signal from abort(3)
       SIGFPE        8       Core    Floating point exception
       SIGKILL       9       Term    Kill signal
       SIGSEGV      11       Core    Invalid memory reference
       SIGPIPE      13       Term    Broken pipe: write to pipe with no
                                     readers
       SIGALRM      14       Term    Timer signal from alarm(2)
       SIGTERM      15       Term    Termination signal
```

Run the command `man 7 signal` to read `signal` command's manual page.


## Environment variables

- What are they?
- How to use them?


## A cheat sheat of commands


| Command    | Description |
|------------|-------------|
| `echo`     |             |
| `cat`      |             |
| `head`     |             |
| `tail`     |             |
|            |             |
| `sed`      |             |
| `awk`      |             |
| `grep`     |             |
| `sleep`    |             |
|            |             |
| `find`     |             |
|            |             |
| `ps`       |             |
| `top`      |             |
| `htop`     |             |
| `kill`     |             |
| `killall`  |             |
|            |             |
| `ping`     |             |
| `netstat`  |             |
|            |             |
| `ifconfig` |             |
| `ip`       |             |
|            |             |
| `hostname` |             |
| `uname`    |             |
|            |             |
| `date`     |             |
| `cal`      |             |
|            |             |
| `clear`    |             |
| `history`  |             |
|            |             |
| `ssh`      |             |
| `scp`      |             |
| `sftp`     |             |
| `ftp`      |             |
| `wget`     |             |
| `curl`     |             |



## Shell builtins

- `type`
- `which`


## Aliases


## Editors

- `nano`
- `vim`
- `emacs`


## Writing shell scripts

The shell also provides a little programming language.  You can write
commands in a file called a _shell script_, and make it executable.
Shell scripts usually have a `.sh` filename extension.

Shell scripts are useful when you need to run some complex sequence of
commands often.

Here is a simple shell script:

```sh
#! /usr/bin/env bash

# A simple script.

echo "Hello world!"
```

<!-- TODO: describe shebang, comments, commands -->

Assuming we name the script `hello.sh`, we can make it executable with
`chmod`, and run `hello.sh`:


```console
[ssasidharan@lnx201 ~]$ chmod +x hello.sh 
[ssasidharan@lnx201 ~]$ ./hello.sh 
Hello world!
```

Bash provides some useful constructs such as loops and functions.

- loops
- functions
- ~/.local/bin or $HOME/bin maybe?


## Nifty: terminal multiplexers

- `tmux`
- `screen`


## Finding help and documentation

- finding help: man, info, the web


## Further reading

- https://missing.csail.mit.edu/2020/shell-tools/
