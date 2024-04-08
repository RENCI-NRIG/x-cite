# Version control

## What is it?

Version control systems are software tools that are used to track
changes to source code or other collections of files.

Some well-known version control systems include: Git, Mercurial,
Subversion, Darcs, Fossil, CVS, and several proprietary systems.  Each
of them vary in practical usage and in implementation details.

Today Git is the most popular one, and seem to have "won", so Git is
what we will be discussing here.

## Why do we need it?

When you work on a project, you often will want to save the state of
your code at various points, such that you can go back and forth
between these various points.  When you work on a project as part of a
team, you will also want to know who wrote some part of the code,
when, and why.

Whether you work alone or in a team, using a version control system
will help you achieve the above goals.

In the absence of a version control system, you will often will end up
with a chaotic mess which achieves the above goals in a poorer manner.
You will likely resort to several almost-same-but-not-quite files
variously named like so:

- `notebook.ipynb`
- `notebook-2024-05-01.ipynb`
- `notebook-working.ipynb`
- `notebook-test.ipynb`

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
installed already.

Here we assume that you are using the shell account that you have with
CLASSE.

```{.bash}
$ git --help
```

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
  
