# Git

How to git successfully even with low background knowledge.

`2020/09/10, Jaroslav Langer`

## MENU

- [Basic information](#basic-information)
- [Create git account](#create-git-account)
- [Git installation and setup](#git-installation-and-setup)
- [Create a project](#create-a-project)
- [Contribute to a project](#contribute-to-a-project)
- [Branching](#branching)
- [Commiting](#commiting)
- [Showing](#showing)
- [Merging](#merging)
- [Remote repositories - remotes](#remote-repositories---remotes)
- [Stash](#stash)
- [Remove changes after commit](#remove-changes-after-commit)
- [Remove changes after push](#remove-changes-after-push)
- [Create the pull request](#create-the-pull-request)
- [Add repository from other git](#add-repository-from-other-git)
- [Add submodule](#add-submodule)


## Basic information

Git is a version control system. Probably the best way to learn it is just to read the [documentation](https://git-scm.com/doc).
In case you do not have much time and just need to jump on the train, this document helps you to understand the basics fast.

Git keeps the versions as a snapshots on your local machine. 
It enables you to work completely offline and synchronize the code with the remote repository when it suits you.

In the git repository, every file can be in three states:
1) modified - the file is changed but you don't want the change to be recorded in the next version (snapshot)
2) staged - the file is changed and the change will be recorded with the next commit (~ the change is added to the index)
3) commited - the change is safely stored in the local git database

clone - clones remote git repository to your machine as local git repository
branch - branch is simply a pointer to specific snapshot (version) 
HEAD - special pointer which point at the branch you are currently on
checkout - changes branch at which the HEAD is pointing and updates the local files to match with that branch (switch branches)
push - pushes local repository the the remote one
fetch - downloads content from remote git repository
merge - incorporates changes from given named branch to current branch
pull - does git fetch and git merge

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

On your GITSITE create a new repository and get its url under button "clone" (e.g. https://github.com/USERNAME/PROJECT.git)

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
[source](https://about.gitlab.com/)

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
[source](https://github.com/)

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

Instead of modifing master, and pushing to the origin/master.
Create a development branch and make the changes there. Don't merge the branch with master.
Push the development branch to remote and let the owner know about it, i.e. let him merge it himself.

```
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

The default branch (and usually the main one) is caled "master".
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

## Commiting

```sh
# Add things for the next commit
git add NAME_OF_FILE

# Add everything to next commit
git add -A # git add --all

# Delete changes from index (not to be commited)
git checkout -- FILENAME

# Delete THING and remove it from being in the next commit
git rm -r THING

# Delete thing which has local modifications
git rm --cached THING # git rm -rf --cached FOLDER_NAME/

# Show status of git files, which where not added, which were deleted but added etc.
git status

# Commit added things
git commit -m "Meaningful comment"
```

[source](https://stackoverflow.com/questions/50167969/how-to-fix-modified-content-untracked-content-in-git)

## Showing

```sh
### Show changes between last merge and last commit
git show

### Show all commits
git log
```
---

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
[No fast-foreward](https://nvie.com/posts/a-successful-git-branching-model/).

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

## Add remote
git remote add NAME URL

## Add remote and fetch
git remote add -f NAME URL

## Delete remote
git remote remove NAME URL
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

[more](#https://git-scm.com/docs/git-reset)

## Remove changes after push

```sh
# Revert some existing commits (Requires no local modifications from the HEAD commit)
git revert
```

---

## Create the pull request

[Create the pull request](#https://git-scm.com/docs/git-request-pull)

---

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
[source](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository)

---

## Add submodule

```sh
git submodule add https://github.com/NEW_REPOSITORY.git REPO_NAME
```

## In case of any troubles

```sh
git help
```

[Documentation](https://git-scm.com/doc)
