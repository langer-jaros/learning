# Git

How to use git successfully even with a little background knowledge.

`2021 Feb 02, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [Basic information](#basic-information)
* [Git --help](#git---help)
* [Create git account](#create-git-account)
* [Git installation and setup](#git-installation-and-setup)
* [Create a project](#create-a-project)
    * [Create repository from scratch](#create-repository-from-scratch)
    * [Create repository from existing folder](#create-repository-from-existing-folder)
    * [Start to work on someones repository (fork)](#start-to-work-on-someones-repository-fork)
* [Contribute to a project](#contribute-to-a-project)
    * [Contribute to someones repository (with push rights)](#contribute-to-someones-repository-with-push-rights)
        * [Update the content from remote](#update-the-content-from-remote)
        * [Develop the code as a new branch](#develop-the-code-as-a-new-branch)
    * [Contribute without the rights to push - fork](#contribute-without-the-rights-to-push---fork)
* [Branching](#branching)
* [Show files status (untracked/modified/added/deleted)](#show-files-status-untrackedmodifiedaddeddeleted)
* [File differences](#file-differences)
* [Add files to or remove from the index](#add-files-to-or-remove-from-the-index)
* [Ignore files from the git structure](#ignore-files-from-the-git-structure)
* [Committing](#committing)
* [Show changes and commits](#show-changes-and-commits)
* [Merging](#merging)
    * [Test a new branch before the merge](#test-a-new-branch-before-the-merge)
* [Remote repositories - remotes](#remote-repositories---remotes)
* [Push and Pull](#push-and-pull)
* [Stash](#stash)
* [Remove unwanted staging of many files](#remove-unwanted-staging-of-many-files)
* [Remove changes after commit](#remove-changes-after-commit)
* [Remove changes after push](#remove-changes-after-push)
* [Create the pull request](#create-the-pull-request)
* [Move repository form one GITSITE_OLD to another GITSITE_NEW](#move-repository-form-one-gitsite_old-to-another-gitsite_new)
* [Duplicate a repository](#duplicate-a-repository)
* [Add submodule](#add-submodule)

<!-- /TOC -->

## Basic information

Git is a version control system. Probably the best way to learn it is just to read the [documentation](https://git-scm.com/doc).
In case you do not have much time and just need to jump on the train, this document helps you to understand the basics fast.

Git keeps the versions as a snapshots on your local machine. 
It enables you to work completely offline and synchronize the code with the remote repository when it suits you.

In the git repository, every file can be in three states:
1) modified - the file is changed but you don't want the change to be recorded in the next version (snapshot)
2) staged - the file is changed and the change will be recorded with the next commit (~ the change is added to the index)
3) committed - the change is safely stored in the local git database

| command  | Description                                                      |
| ---      | ---                                                              |
| clone    | Clones remote git repository to your machine as local git repository. |
| branch   | Branch is simply a pointer to specific snapshot (version).       |
| HEAD     | Special pointer which point at the branch you are currently on.  |
| checkout | Changes branch at which the HEAD is pointing and updates the local files to match with that branch (switch branches). |
| push     | Pushes local repository to the remote one.                       |
| fetch    | Downloads content from remote git repository.                    |
| merge    | Incorporates changes from given named branch to current branch.  |
| pull     | Does git fetch and git merge.                                    |

## Git --help

Git has a beautifully done manual, so adding `--help` after any command is usually sufficient help once you start using the git.

```sh
# Example of help for rm command
git rm --help
```

## Create git account

First step is to create account on some git site such as GitHub, GitLab etc.

Once you have it, add your public SSH key to it.

## Git installation and setup

After the git installation, there is a need of some configurations.

```sh
git config --global user.name "Name Surname"
git config --global user.email "username@email.com"
```

## Create a project

It is either possible to create a new repository (project) or to find some already existing.

### Create repository from scratch

On your GITSITE create a new repository and get its URL under button "clone" (e.g. https://github.com/USERNAME/PROJECT.git)

```sh
# Clone the repository (project) to your machine
git clone git@YOUR_PROJECT_PATH.git

# Create README.md about your project
echo "# REPOSITORY_NAME" >> README.md #touch README.md

# Add the README.md to the index
git add README.md

# Record changes to the repository with comment
git commit -m "Initial commit, readme created"

# Pushes the local commit to the remote site, the clone have set origin to git@YOUR_PROJECT_PATH.git
git push -u origin master
```

* [From gitlab.com](https://about.gitlab.com/)

### Create repository from existing folder

```sh
cd EXISTING_FOLDER
echo "# REPOSITORY_NAME" >> README.md #touch README.md

# Create an empty Git repository or reinitialize an existing one
git init

# Add the local things for next commit
git add . # git add README.md # git add --all

# Commits the added content
git commit -m "First commit"

# Adds remote site git@GITSITE:USER/REPOSITORY.git as origin
git remote add origin git@GITSITE.com:USER_NAME/REPOSITORY_NAME.git

# Push the local content to master branch of origin
git push -u origin master
```

* [From github.com](https://github.com/)

### Start to work on someones repository (fork)

There is an option to use an existing project as your starting point by making a copy.
It is called a fork, by doing so you will have your own copy of the whole project.
Then you can just git clone and start doing stuff.

## Contribute to a project

### Contribute to someones repository (with push rights)

```sh
# Clone the repository
git clone git@GITSITE.com:PROJECT_PATH.git
```

#### Update the content from remote

If there is a time lag between cloning and the time you want to work on the repository, the remote repository may have changed.
Then it is reasonable to update the local content from the remote i.e. pull the changes.

```sh
git checkout master
# Git pull fetches the last version from the origin (GITSITE:repo) and merges it with the local content
git pull # git pull origin 
```

#### Develop the code as a new branch

Instead of modifying master, and pushing to the origin/master.
Create a development branch and make the changes there. Don't merge the branch with master.
Push the development branch to remote and let the owner know about it, i.e. let him merge it himself.

```bash
# Create your development branch
git branch BRANCH_NAME

# Check out the branch
git checkout BRANCH_NAME

# Record the changes to be commited 
git add PATH_TO_FILE, PATH_TO_FILE_1

# Check if everything is git added or git deleted
git status

# Commit the changes
git commit -m "Meaningful description of the changes"

# Push the local changes to the branch BRANCH_NAME of remote site
git push -u origin BRANCH_NAME
```

### Contribute without the rights to push - fork

Fork the repository. Clone it and treat it as your own.

Once you are happy with your changes, create a pull request on the GITSITE. 

## Branching

The default branch (and usually the main one) is called "master".
It is handy to create a new branch once you want to create new feature.

```sh
# Show branches - the current is marked with asterix
git branch

# List all branches, also the remote ones 
git branch -a

# Create branch
git branch BRANCH_NAME

# Change to a branch
git checkout BRANCH_NAME

# Change the current branch to master
git checkout master

# Crate branch and check out to it in one step
git checkout -b BRANCH_NAME

# Delete branch
git branch -d BRANCH_NAME

# Rename branch
git branch -m NEW_BRANCH_NAME
```

## Show files status (untracked/modified/added/deleted)

```sh
# Show status of git files, which where not added, which were deleted but added etc.
git status
```

## File differences

```sh
# Show file last change (difference between the file and it's index representation)
git diff path/to/file.sth
```

## Add files to or remove from the index

```sh
# Add file contents to the index (file will be commited)
git add NAME_OF_FILE
# Add everything to the index (everything will be commited)
git add -A # git add --all

# Discard changes in working directory
git checkout -- FILENAME

# Remove files from the working tree and from the index (File is deleted and will not be commited)
git rm FILE
git rm -r DIR # Recursive (directory) option
git rm --cached FILE # Remove FILE only from index (will not be commited) dont delete it locally.
git rm -f FILE # Force the removal - remove file from index and directory even when it has local modifications
```

* [source](https://stackoverflow.com/questions/50167969/how-to-fix-modified-content-untracked-content-in-git)

## Ignore files from the git structure

`.gitignore` file specifies intentionally untracked files to be ignored.

```.gitignore
# Ignore all .ipynb checkpoints
.ipynb_checkpoints
# Ignore knapsack instances directory
./knapsack/instances
```

* [gitignore (git-scm.com)](https://git-scm.com/docs/gitignore)
* [How to git ignore ipython notebook checkpoints anywhere in repository (stackoverflow.com)](https://stackoverflow.com/questions/35916658/how-to-git-ignore-ipython-notebook-checkpoints-anywhere-in-repository)

## Committing

```sh
# Commit added things
git commit -m "Meaningful comment"
```

## Show changes and commits

```sh
# Show changes between last merge and last commit
git show

# Show all commits
git log

# Show commits affecting the a specific file
git log --oneline path/to/file.sth

# File difference to specific commit from the previous step
git diff 0a42637 path/to/file.sht
```

* [git diff file against its last change (stackoverflow.com)](https://stackoverflow.com/questions/10176601/git-diff-file-against-its-last-change)


## Merging

Merge the NEW_BRANCH to master at origin 

```sh
git checkout master

git merge NEW_BRANCH

git push origin master
```

```sh
# Merge the local content with BRANCH_NAME of REMOTE_NAME
git merge --allow-unrelated-histories REMOTE_NAME/BRANCH_NAME

# No fast-foreward (--no-ff)
git merge --no-ff BRANCH_NAME
```

* [No fast-foreward - A successful Git branching model (nvie.com)](https://nvie.com/posts/a-successful-git-branching-model/).

### Test a new branch before the merge

```sh
# Fetch the file from origin (remote site)
git fetch origin

# Create the desired BRANCH_NAME from origin and change to it 
git checkout -b BRANCH_NAME origin/BRANCH_NAME

git merge master
```

## Remote repositories - remotes

Once you clone a repository, it sets a remote for the repository under the origin.
Thanks to that you can push your code to origin (the remote repository) or to pull code from the repository.

```sh
# Show the remotes
git remote -v

# Add remote
git remote add NAME URL

# Add remote and fetch
git remote add -f NAME URL

# Delete remote
git remote remove NAME URL

# Set remote url
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

## Push and Pull

```sh
# Pushes the code to the origin
git push -u origin

# Git pull - equivalent to git fetch and git merge
git pull

# Downloads content from a remote repository and write to .git/FETCH_HEAD
git fetch 
# Merges the FETCH_HEAD to local repo
git merge FETCH_HEAD
```

## Stash

Save the changes from the last commit on and clean them

So the working directory is at the stage of last commit.

```sh
# Saves all differences from last commit away and clean them off
git stash

# List the stashes
git stash list

# See the most recent stash
git stash show -p # git stash show -p stash@{0}

# See older stash
git stash show -p stash@{1}

# Drop the stash
git stash drop
```

## Remove unwanted staging of many files

```sh
git reset
```

## Remove changes after commit

Reset current head to the specific state (commit)

```sh
# Reset the HEAD to the given commit, files are untouched but not marked for commit
git reset HASH_OF_COMMIT #~ git reset --mixed HASH_OF_COMMIT

# Reset the index and the working direcotry - leaves everything at the stage of the commit
git reset --hard HASH_OF_COMMIT

# Reset only the HEAD, but the working directory and index are the same
git reset --soft HASH_OF_COMMIT
```

* [git-reset (git-scm.com)](#https://git-scm.com/docs/git-reset)

## Remove changes after push

```sh
# Revert some existing commits (Requires no local modifications from the HEAD commit)
git revert
```

## Create the pull request

* [Create the pull request](#https://git-scm.com/docs/git-request-pull)

## Move repository form one GITSITE_OLD to another GITSITE_NEW

```sh
git clone git@GITSITE_OLD.com:USER/PROJECT.git # cd existing_git_repo
git remote rename origin old-origin
git remote add origin git@GITSITE_NEW.com:USER/PROJECT.git
git push -u origin --all
git push -u origin --tags
```

## Duplicate a repository

```sh
git clone --bare https://githost.org/OLD_REPOSITORY.git

cd OLD_REPOSITORY.git

git push --mirror https://github.com/NEW_REPOSITORY.git

cd ..

rm -rf NEW_REPOSITORY.git
```

* [source](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository)

## Add submodule

```sh
git submodule add https://github.com/NEW_REPOSITORY.git REPO_NAME
```

