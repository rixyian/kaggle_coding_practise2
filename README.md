# kaggle_coding_practise2

practise corner for getting used to python again, and to Kaggle and Keras

## remember for starting new Git projects:

git clone doesn't create a git folder, so:

1. First make the repo on github, and check that the branch is set to "main", or whatever branch name
2. From the folder above where the local repo folder will be, do `git clone` in order to pull the folder containing whatever was just made on the remote repo
3. Then go into that newly created folder to run `git init` and officially connect the folder to the branch & remote head in order to push commits to it from local stack

## venv things to remember
Need to use a new venv for every new project in order to keep project-specific libraries & modules separate without risk of cross-contamination
1. Use `python -m venv [path of location of folder that'll contain everything to do with the venv, the folder's name being the name of the venv]`
2. Now that the basis of the venv and it's contents / installed libraries & modules have a home in the current directoy: use `. my_virt_env/Scripts/activate` to enter the virtual environment

    * it'll show the venv's name from step 1 in brackets at start of CLI prompt when venv is currently on
3. and in the same directory, `deactivate` to turn venv off
4. Make sure to regularly use `pip freeze > requirements.txt` to record the installations that this venv's pip has done and is keeping track of
    * This ensures that if someone else pulls this branch on github and downloads this project, the reqs file can be used by venv to automatically install the specific modules & library versions that project separate to that of any other project

Seems like when in venv state, you can still interact with things in file sys and create new files that can be found via File Explorer, it's just any libraries & modules installed that'll be isolated in this environment

## python things to remember

* 