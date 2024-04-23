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

<!-- - `notebook.ipynb` -->
<!-- - `notebook-2024-05-01.ipynb` -->
<!-- - `notebook-2024-05-01-final.ipynb` -->
<!-- - `notebook-working.ipynb` -->
<!-- - `notebook-test.ipynb` -->
<!-- - `notebook-final.ipynb` -->

[![](http://www.phdcomics.com/comics/archive/phd101212s.gif)][notfinal]

[notfinal]: https://phdcomics.com/comics/archive.php?comicid=1531

This scheme is basically a messy reinvention of a version control
system.  That might work in the simple cases, but it will soon break
down as you do more work on your project.

Instead, what you want to do is learn to use a version control system
properly.  You want to avoid the cognitive overload of dealing with
messy schemes based on filenames.


## Version control in practice: Git

As stated above, Git is the most popular version control system in use
today.  Git is a command-line program that runs on all popular
operating systems.  If you use macOS or Linux, you probably have Git
installed already.  Here we assume that you are using the account that
you have with CLASSE.

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

<!-- TODO: elaborate -->

### Generating ssh keys

```{.bash}
$ ssh-keygen -t rsa -b 4096 -C "you@example.com"
```

<!-- TODO: elaborate ssh public and private keys -->

### Initial configuration

<!-- TODO: elaborate -->

```{.bash}
$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com
```

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
  
