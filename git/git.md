# How to GIT

`2020/03/15, Jaroslav Langer`

## MENU

+ [Absolute start with git](#absolute-start-with-git)
+ [Start using git (basics)](#start-using-git-(basics))
+ [Showing](#showing)
+ [Create a merge request](#create-a-merge-request)
+ [Delete folder from git competence](#delete-folder-from-git-competence)
+ [Create repository from existing git repository](#create-repository-from-existing-git-repository)

## Absolute start with git

First step is to create git repository (project) on a git site.

(First step may actually be to create the fork on Git page)


### Git global setup - to be recognizable

```sh
git config --global user.name "Name Surname"
git config --global user.email "username@email.com"
```

### Creation of a repository from scratch

```sh
# Clone the repository (project) to your machine
git clone git@YOUR_PROJECT_PATH.git

# Create README.md about your project
echo "# rep_name" >> README.md #touch README.md

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
cd existing_folder
echo "# rep_name" >> README.md #touch README.md

#Create an empty Git repository or reinitialize an existing one
git init
git add .
git commit -m "first commit"

# Adds remote origin for the repository at git@GITSITE:USER/REPOSITORY.git
git remote add origin git@github.com:acc_name/rep_name.git
git push -u origin master
```
[source](https://github.com/)

## Start using git (basics)

### Change the current branch (to master):

```sh
git checkout master
```

### Update the folders to current state:

```sh
git pull
```

### Create a new branch:

```sh
git branch YOUR_BRANCH_NAME
```
**Or**
```sh
git checkout -b YOUR_BRANCH_NAME
```

### Delete branch

```sh
git branch -d branch_name
```

---

## Showing 

### Show current branch

```sh
git branch
```

### Show changes between last merge and last commit

```sh
git show
```

---

## Create a merge request

### Add files for commit (or -all)

```sh
git add --all
``` 
**Or** 

```sh
git add -A
```

### Show status of git files

```sh
git status
```

### Commit

```sh
git commit -m "Meaningful comment."
```

### Push merge request to the master

```sh
git push -u origin NAME_OF_BRANCH
```

### Test a new branch before the merge

```sh
git fetch origin
git checkout -b BRANCH_NAME origin/BRANCH_NAME
git merge master
```

---

## Merge the new branch 

```sh
git checkout master
```

--no-ff means no fast-foreward [More information](https://nvie.com/posts/a-successful-git-branching-model/).

```sh
git merge --no-ff BRANCH_NAME
git push origin master
```

---

## Delete folder from git competence

> If you added this path by mistake, you can remove it from the index with:
```sh
git rm --cached FOLDER_NAME
```
**or**
```sh
git rm -rf --cached FOLDER_NAME/
```
[source](https://stackoverflow.com/questions/50167969/how-to-fix-modified-content-untracked-content-in-git)

## Create repository from existing git repository

```sh
cd existing_git_repo
git remote rename origin old-origin
git remote add origin git@GITSITE.com:USER/PROJECT.git
git push -u origin --all
git push -u origin --tags
```

---

In case of any troubles

```sh
git help
```

[Documentation](https://git-scm.com/doc)
