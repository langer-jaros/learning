# How to GIT

```2020/03/03, Jaroslav Langer```

## MENU
+ [Absolute start with git](#absolute-start-with-git)
+ [Showing](#showing)
+ [Create a merge request](#create-a-merge-request)
+ [Delete folder from git competence](#delete-folder-from-git-competence)
+ [Create a repository (command line)](#create-a-repository-(command-line))

## Absolute start with git
(First step may actually be to create the fork on Git page)

### Make a clone of the project into your folder:
```
git clone git@YOUR_PROJECT_PATH.git
```
### Change the current branch (to master):
```
git checkout master
```
### Update the folders to current state:
```
git pull
```
### Create a new branch:
```
git branch YOUR_BRANCH_NAME
```
**Or**
```
git checkout -b YOUR_BRANCH_NAME
```
### Delete branch
```
git branch -d branch_name
```
---
## Showing 
### Show current branch
```
git branch
```
### Show changes between last merge and last commit
```
git show
```
---
## Create a merge request
### Add files for commit (or -all)
```
git add --all
``` 
**Or** 
```
git add -A
```
### Show status of git files
```
git status
```
### Commit
```
git commit -m "Meaningful comment."
```
### Push merge request to the master
```
git push -u origin NAME_OF_BRANCH
```
### Test a new branch before the merge
```
git fetch origin
git checkout -b BRANCH_NAME origin/BRANCH_NAME
git merge master
```
---
## Merge the new branch 
```
git checkout master
```
--no-ff means no fast-foreward [More information](https://nvie.com/posts/a-successful-git-branching-model/).
```
git merge --no-ff BRANCH_NAME
git push origin master
```
---
## Delete folder from git competence
> If you added this path by mistake, you can remove it from the index with:
```
git rm --cached FOLDER_NAME
```
**or**
```
git rm -rf --cached FOLDER_NAME/
```
[source](https://stackoverflow.com/questions/50167969/how-to-fix-modified-content-untracked-content-in-git)

---

In case of any troubles
```
git help
```

## Create a repository (command line)
```
echo "# rep_name" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:acc_name/rep_name.git
git push -u origin master
```
[source](https://github.com/)


