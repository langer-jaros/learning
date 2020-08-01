# Git

How to git successfully even with low background knowledge.

`2020/08/01, Jaroslav Langer`

## MENU

- [Absolute start with git](#absolute-start-with-git)
- [Start using git (basics)](#start-using-git-(basics))
- [Bit advanced](#bit-advanced)

## Absolute start with git

### Git account

First step is to create account on some git site such as GitHub, GitLab etc.

Once you have it, add a public key to it.

### Git installation and setup

After the terminal git installation, there is a need of some configurations.

```sh
git config --global user.name "Name Surname"
git config --global user.email "username@email.com"
```

### Creation of a project

It is either possible to create a new repository (project) or to fork some already existing.

Both can be easily done on the git website. 

### Create repository from scratch

```sh
# Clone the repository (project) to your machine
git clone git@YOUR_PROJECT_PATH.git

# Create README.md about your project
echo "# REPOSITORY_NAME" >> README.md #touch README.md

# Add the README.md to the index
git add README.md

# Record changes to the repository with comment
git commit -m "add README"

# Update remote references with local ones
git push -u origin master
```
[source](https://about.gitlab.com/)

### Create repository from existing folder

```sh
cd EXISTING_FOLDER
echo "# REPOSITORY_NAME" >> README.md #touch README.md

#Create an empty Git repository or reinitialize an existing one
git init

# Add the local things for next commit
git add .

# Commits the added content
git commit -m "first commit"

# Adds remote origin for the repository at git@GITSITE:USER/REPOSITORY.git
git remote add origin git@GITSITE.com:USER_NAME/REPOSITORY_NAME.git

# Push the local content to master branch of origin
git push -u origin master
```
[source](https://github.com/)

## Start using git (basics)

### Branches

There can be many branches, the one above all is called master

```sh
# Show your current branch
git branch

# List branches
git branch -a

# Change the current branch to master
git checkout master

# Create branch
git branch BRANCH_NAME

# Change to a branch
git checkout BRANCH_NAME

# Crate and change to it in one step
git checkout -b BRANCH_NAME

# Delete branch
git branch -d BRANCH_NAME

# Rename branch
git branch -m NEW_BRANCH_NAME
```

### Update the master branch

If you have cloned the repository and others may have changed it, it is reasonable to update the content.

```sh
# Fetch the most recent content from the git site and merge it with the old one 
git pull origin
```

### Commiting

```sh
# Add things for the next commit
git add NAME_OF_FILE

# Add everything to next commit
git add -A #OR git add --all

# Delete changes from index (not to be commited)
git checkout -- FILENAME

# Delete THING and remove it from being in the next commit
git rm -r THING

# Delete thing which has local modifications
git rm --cached THING

# OR
git rm -rf --cached FOLDER_NAME/

# Show status of git files, which where not added, which were deleted but added etc.
git status

# Commit added things
git commit -m "Meaningful comment."
```

[source](https://stackoverflow.com/questions/50167969/how-to-fix-modified-content-untracked-content-in-git)

### Remotes

The master branch is (should be) above all your branches, still they are all on your machine.

When you want to collaborate with others, the code is passed to a remote repository.

Remote repository is the one you have created on the git site.

The main remote is named origin and it is the one where you cloned your project from.

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

### Showing 

```sh
### Show changes between last merge and last commit
git show

### Show all commits
git log
```
---

### Create a merge request

```sh
# Add the file for commit
git add PATH_TO_FILE

# Commit it
git commit -m "Commit comment"

# Push the NAMO_OF_BRANCH to the origin (remote site)
git push -u origin NAME_OF_BRANCH

# Go to GIT_SITE and create merge request 
``` 

### Merging

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


### Bit advanced

### Stash

Save the changes from the last commit on and clean them

So the working directory is at the stage of last commit.

```sh
# Saves all differences from last commit away and clean them off
git stash

# List the stashes
git stash list

# See the most recent stash
git stash show -p #OR git stash show -p stash@{0}

# See older stash
git stash show -p stash@{1}

# Drop the stash
git stash drop
```

### Create repository from existing git repository

```sh
cd existing_git_repo
git remote rename origin old-origin
git remote add origin git@GITSITE.com:USER/PROJECT.git
git push -u origin --all
git push -u origin --tags
```

---

### Create the pull request

[Create the pull request](#https://git-scm.com/docs/git-request-pull)

### Test a new branch before the merge

```sh
# Fetch the file from origin (remote site)
git fetch origin

# Create the desired BRANCH_NAME from origin and change to it 
git checkout -b BRANCH_NAME origin/BRANCH_NAME

git merge master
```

---

### Add repository from other git

git clone --bare https://githost.org/OLD_REPOSITORY.git

cd OLD_REPOSITORY.git

git push --mirror https://github.com/NEW_REPOSITORY.git

[source](https://stackoverflow.com/questions/30268549/mirroring-from-gitlab-to-github)

---

### Add submodule

```sh
git submodule add https://github.com/NEW_REPOSITORY.git REPO_NAME
```

In case of any troubles

```sh
git help
```

[Documentation](https://git-scm.com/doc)
