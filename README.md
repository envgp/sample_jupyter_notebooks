# sample_jupyter_notebooks
Sample jupyter notebooks showing some python basics and geophysical data analysis. Best used with Google Colab.


# A basic and quick git crash course:


### topics to be covered
* What is GitHub
* What are repos/repositories
* How to clone a repository
* How to add changes
* How to commit changes
* How to open a PR for peer review/merging


### What is the purpose of git? 
Have you ever been in either of these scenarios? (I have): 

1. you had some code that worked, you changed something and broke it, and wished you could quickly go back to the working state without desperately using ctrl + z?
2. Tried to share some code you wrote with someone, only to have it be difficult to install on their machine? 

These are the problems that github solves (also others)
- seogi michael others please chime in with details i miss or questions

Git is a command line-based distributed version control system. Version control system means that its goal is to track and record every change in a set of text files (typically source code, but not exclusively), collectively called a repository. It then possible to check what every changes contained and when it occurred, and to recover and return to any previous state of the tracked files.

Distributed means that these tracked files can be stored on many different computer systems, such as a local computer, remote servers, or in the cloud. None plays the role of main copy, they are all equivalent, and users can synchronise (pull and push) code from one to another.


### Key concepts
* remote - the 'cloud' or a server where your codes are hosted
* local - your physical machine where you are editing codes and testing the changes

![alt text](https://res.cloudinary.com/practicaldev/image/fetch/s--M_fHUEqA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/128hsgntnsu9bww0y8sz.png)


### outline + commands + workflow 

* How to clone a repository
    * clone michael’s repo - follow along 
    * open command line and type:
    * `git clone https://github.com/envgp/sample_jupyter_notebooks`
    * Show also how to create repo from scratch
    * type `git status` to see what changes have been made 

* What are repos/repositories
    * How to structure your repo [how I do it..]
    * `PROJECT_NAME/`
        * `code/`
            * `00_preprocess.py`
            * `01_prep_data.py`
            * `02_method.py`
            * `03_plot_results.py`
        * `data/`
            * `source1/`
            * `source2/`
        * `shape/`
            * `shapefile1.kml`
        * `results/`
            * `model1_results.csv`
            * `model2_results.csv`
        * `figures/`
            * `figure1.png`
            * `figure2.png`

* How to add changes

    * How to create a new branch 
        * `git branch branchname`
    * How to add a new file to a repository
        * `git add filename.py`
    * how to switch branches 
        * `git checkout branchname`
    * how to modify an existing file 
        * make your changes 
        * 1git add changed_file.py`
        
* How to commit changes (`-m` flag specifies "write a message with this commit")
    * `git commit -m 'description of changes'`  
* How to add your new branch
    * `git push --set-upstream origin et_branch`
* How to open a PR for peer review/merging
    * merge from GUI 
* How to update your local repo
    * `git pull` 
