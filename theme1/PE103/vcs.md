# Version Control

Version control systems (or VCS) are software tools that are used to
track changes to source code or other collections of files.

Wikipedia has a [fairly long list][vcs-list] of version control
systems, each of them varying in practical usage and in implementation
details.

Today Git is the most popular version control system in use. Git
appears to have "won", so Git is what we will be discussing here.

[vcs-list]: https://en.wikipedia.org/wiki/List_of_version-control_software


## Why do we need version control?

When you work on a project, you often will want to save the state of
your code at various points, such that you can go back and forth
between these various points.  When you work on a project as part of a
team, you will also want to know who wrote some part of the code,
when, and why.

Whether you work alone or in a team, using a version control system
will help you achieve the above goals.  Sometimes your team member is
the past you (who should help you), or the future you (whom you should
help).

In the absence of a version control system, you will often will end up
with a chaotic mess which achieves the above goals in a poorer manner.
You will likely resort to several almost-same-but-not-quite files
variously named like so:

- `notebook.ipynb`
- `notebook-2024-05-01.ipynb`
- `notebook-2024-05-01-final.ipynb`
- `notebook-working.ipynb`
- `notebook-test.ipynb`
- `notebook-final.ipynb`

Or a situation depicted by a famous PHD Comics [strip][notfinal]:

[![](http://www.phdcomics.com/comics/archive/phd101212s.gif)][notfinal]

[notfinal]: https://phdcomics.com/comics/archive.php?comicid=1531

This scheme is basically a messy reinvention of a version control
system.  That might work in the simple cases, but it will soon break
down as you do more work on your project.

You want to avoid the cognitive overload of dealing with messy schemes
based on file names.  You want to use a version control system
properly.


## Version control in practice: Git

Git is a command-line program that runs on all popular operating
systems.  If you use macOS or Linux, you probably have Git installed
already.  Here we assume that you are using the account that you have
with CLASSE.

You can start trying out `git` by running the below in a terminal:

```{.bash}
$ git --help
```

These very notes that you are currently reading are version controlled
using Git.  They are hosted at the _repository_ at
<https://github.com/RENCI-NRIG/X-CITE/>.  You can _clone_ that
repository using `git clone` command:

```{.bash}
$ git clone https://github.com/RENCI-NRIG/X-CITE.git
Cloning into 'X-CITE'...
remote: Enumerating objects: 948, done.
remote: Counting objects: 100% (485/485), done.
remote: Compressing objects: 100% (266/266), done.
remote: Total 948 (delta 228), reused 421 (delta 172), pack-reused 463
Receiving objects: 100% (948/948), 4.52 MiB | 0 bytes/s, done.
Resolving deltas: 100% (446/446), done.
```

You just have obtained a _clone_ of X-CITE course repository in a
local directory named `X-CITE`.  You can `cd` into that directory now
with `cd X-CITE`, and then run some `git` commands such as `git
status` and `git log` there:

```{.bash}
$ cd X-CITE/
$ git status
# On branch main
nothing to commit, working directory clean
$ git log
commit fd95497e30827d52dd99855a0e1be99b3db4282e
Author: Sajith Sasidharan <sajith@hcoop.net>
Date:   Mon Apr 22 09:27:27 2024 -0500

    Mention the trace module

commit 7d55b104b50f8b1f5b8201765ceac8541f9543df
Author: Sajith Sasidharan <sajith@hcoop.net>
Date:   Mon Apr 22 09:16:44 2024 -0500

    Add a line

[... more output, elided for brevity ...]
```

If you are new to version control in general and Git in particular,
you will need to understand some concepts (such as _repositories_,
_cloning a repository_, _commits_, _log messages_, _branches_) in
order to understand what just happened above. Let us unpack stuff.


## Git concepts

<!-- TODO: elaborate -->

- commits
- staging area
- remotes
- branches

## Getting started with Git

Git commands are generally of the form `git <subcommand>`, where
`<subcommand>` is for the specific operation you want to do.  We will
discuss them in the following sections.

There is also a little bit of configuration that you should do, before
you are able to `git add` and `git commit` your changes.  Let us start
with this configuration.


### Initial configuration

Git keeps track of who makes changes.  For this to work, you'll need
to configure Git using `git config` subcommand:

```{.bash}
$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"
```

This will write configuration to a file named `.gitconfig` in your
home directory.

```{.bash}
$ cat ~/.gitconfig
[user]
	name = Your Name
	email = you@example.com
```

Of course, you should use "real" values instead of `Your Name` and
`you@example.com`.


### Starting a new repository

Let us start with a very simple example, just for practice.

On `lnx201`, let us create a new directory (with `mkdir hello-world`),
change to that directory (with `cd hello-world`), create a file in
that repository, and initialize a git repository there (with `git
init`):

```{.bash}
$ mkdir hello-world
$ cd hello-world/
$ echo "hello $USER"
hello ssasidharan
$ echo "hello $USER" > hello.txt
$ cat hello.txt
hello ssasidharan
$ git init
Initialized empty Git repository in /home/ssasidharan/hello-world/.git/
```

That created an empty repository, meaning, nothing has been added to
it.  Running `git status` will show an "untracked file":

```{.bash}
$ git status
# On branch master
#
# Initial commit
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	hello.txt
nothing added to commit but untracked files present (use "git add" to track)
```

### Adding changes

Let us add `hello.txt` to the repository, and check the status again:

```{.bash}
$ git add hello.txt
$ git status
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#	new file:   hello.txt
#
```

The command `git add hello.txt` adds the file `hello.txt` to the
repository.  You could also have done a `git add .` to add all files
in the directory to the repository.

Note that `git add hello.txt` does not _commit_ `hello.txt` to the
repository; it just tells Git to pay attention to the file.  With `git
status`, we can see that Git is aware of the fact that there are some
changes to be committed in the repository.


### Committing changes

Use `git commit` to actually commit the tracked file to the
repository:

```{.bash}
$ git commit -m "Add hello.txt"
[master (root-commit) 708bfca] Add hello.txt
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt
```

The string following `-m` option (`-m` is short for `--message`) is a
_commit message_.  You use commit messages to describe the change in a
single short line.

Over time, your commit messages will tell the story about how your
project evolved.  Note that commit messages are not required to be
single lines. You can configure an editor for writing commit messages,
and can write longer commit messages.  More detailed commit messages
would be quite useful when you revisit the change at some point in the
future.

Now we can use `git status` to re-check status of the repository:

```{.bash}
$ git status
# On branch master
nothing to commit, working directory clean
```

We can use `git log` to view the commit history:

```{.bash}
$ git log
commit 708bfcafe32528e90e1d52fd6b94f0c44476518a
Author: Sajith Sasidharan <ssasidharan@lnx201.classe.cornell.edu>
Date:   Tue Apr 23 19:10:02 2024 -0400

    Add hello.txt
```

Let us add some more changes, and commit them:

```{.bash}
$ echo "hello from $HOSTNAME" >> hello.txt
$ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#	modified:   hello.txt
#
no changes added to commit (use "git add" and/or "git commit -a")
$ git add hello.txt
$ git commit -m "Update hello.txt"
[master 233c748] Update hello.txt
 1 file changed, 1 insertion(+)
$ git status
# On branch master
nothing to commit, working directory clean
$ git log
commit 233c748ad3dd31c11a3bc12d0cf106d7fe888fc3
Author: Sajith Sasidharan <ssasidharan@lnx201.classe.cornell.edu>
Date:   Tue Apr 23 19:22:29 2024 -0400

    Update hello.txt

commit 708bfcafe32528e90e1d52fd6b94f0c44476518a
Author: Sajith Sasidharan <ssasidharan@lnx201.classe.cornell.edu>
Date:   Tue Apr 23 19:10:02 2024 -0400

    Add hello.txt
```


### Reviewing changes

We have `git status` and `git log` in action already.  Another command
is `git diff`, which is used to find the difference between two commits:

```{.bash}
$ git diff 708bfcafe32528e90e1d52fd6b94f0c44476518a 233c748ad3dd31c11a3bc12d0cf106d7fe888fc3
diff --git a/hello.txt b/hello.txt
index c5d1025..3f4c47c 100644
--- a/hello.txt
+++ b/hello.txt
@@ -1 +1,2 @@
 hello ssasidharan
+hello from lnx201.classe.cornell.edu
```

A useful shortcut is `git diff HEAD~`:

```{.bash}
$ git diff HEAD~
diff --git a/hello.txt b/hello.txt
index c5d1025..3f4c47c 100644
--- a/hello.txt
+++ b/hello.txt
@@ -1 +1,2 @@
 hello ssasidharan
+hello from lnx201.classe.cornell.edu
```

In Git parlance, `HEAD` implies the last commit on the current branch,
and `HEAD~` is the commit before that, and `git diff HEAD~` would
print the difference between the latest commit and the one before
that.

Eventually, once there are more commits in the repository, you can
view the difference with an arbitrary number of commits in history
with `git diff HEAD~~~` (or, more conveniently: `git diff HEAD~3`),
and so on.  You get the idea.

Another shortcut for those really long commit hashes is using a
smaller prefix of them.  You can find these "short hashes" with `git
log --abbrev-commit` or `git log --oneline`:

```{.bash}
$ git log --oneline
233c748 Update hello.txt
708bfca Add hello.txt
$ git diff 708bfca 233c748
diff --git a/hello.txt b/hello.txt
index c5d1025..3f4c47c 100644
--- a/hello.txt
+++ b/hello.txt
@@ -1 +1,2 @@
 hello ssasidharan
+hello from lnx201.classe.cornell.edu
```


### Ignoring (some) files

Some files just should not be under version control.  Examples would
be:

- Anything generated by a build process, or a compiler, or a test
  suite, or some such.  You do not want to commit the byte-compiled
  `.pyc` files, for example.
- Secrets, or files containing secrets (such as passwords, or tokens).
- Editor configuration files.

You should tell Git to ignore these files by adding their names to a
`.gitignore` file, with one name on a line, so that `git status` will
ignore them.  You can use wildcard patterns such as `*.pyc`.

Take a look at X-CITE course's [.gitignore] for an example.

[.gitignore]: https://github.com/RENCI-NRIG/X-CITE/blob/main/.gitignore


## Working with branches

```{.bash}
$ git branch
$ git merge
```

## Working with tags

```{.bash}
$ git tag
```

## Working with remote repositories

```{.bash}
$ git clone
$ git fetch
$ git pull
$ git push
```

### Generating ssh keys

```{.bash}
$ ssh-keygen -t rsa -b 4096 -C "you@example.com"
```

<!-- TODO: elaborate ssh public and private keys -->


## Git subcommands

<!-- TODO: elaborate -->

```{.bash}
$ git init
$ git add
$ git commit
$ git log
$ git diff
$ git merge
$ git status
$ git branch
$ git clone
$ git fetch
$ git pull
$ git push
```

## GitHub

[GitHub.com](https://github.com/) is what is known as a software
"forge": it is a Git hosting service that can host your source code,
and provide additional services (such as bug tracking, code reviews,
continuous integration, etc) that helps you collaborate with other
people.


## Alternatives to GitHub

While GitHub happens to be the most popular software forge, many
others exist too:

 - [Gitlab.com](https://gitlab.com)
 - [BitBucket.com](https://bitbucket.org/)
 - [Codeberg.org](https://codeberg.org/)

Some people prefer to self-host a forge, and some people prefer no
forge at all. Since Git is a /distributed/ version control system, and
you should be able to collaborate with no forge at all: you can share
your changes as email attachments, if you want.


## Exercises

1. Create an account on GitHub.com, if you do not have an account
  there already.

2. Create a new repository on GitHub.com.  Push some code that you are
  working on to that repository.  If your project is not under version
  control, you will want to do that now.

3. Add some changes to the code. Commit the code. Push those commits
  also to the Git repository.

4. Create a "tag" (based on today's date, or a version number), and
  push the tag to your repository.

## References

- [Pro Git][pro-git]
- [Git cheat sheet][cheat-sheet]

[pro-git]: https://git-scm.com/book/en/v2
[cheat-sheet]: https://education.github.com/git-cheat-sheet-education.pdf
