# Jaroslav Langer
# 11/09/2019

### Absolute start with git
# Make a clone of the project into your folder
git clone git@YOUR_PROJECT_PATH.git
# Change the current branch (to master)
git checkout master
# Update the folders to current state
git pull
# Create a new branch
git branch YOUR_BRANCH_NAME
###

# Show current branch
git branch

# Show changes between last merge and last commit
git show

### Create a merge request
# Add files for commit (or -all)
git add --all
# Show status of git files
git status
# Commit
git commit -m "Meaningful comment."
# Push merge request to the master
git push -u origin NAME_OF_BRANCH
###

### Test a new branch before the merge
git fetch origin
git checkout -b BRANCH_NAME origin/BRANCH_NAME
git merge master
###

### Merge the new branch 
git checkout master
# --no-ff means no fast-foreward 
#  more: https://nvie.com/posts/a-successful-git-branching-model/
git merge --no-ff BRANCH_NAME
git push origin master
###

# In case of any troubles
git help