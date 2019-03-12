# GitCommands
Trying to pull files from my Github repository: “refusing to merge unrelated histories”  

 Solved by this command: 

```
$ git pull origin master --allow-unrelated-histories

```
### Necessary Commands for git:
1. Basic Commands:
2. Marge Commands:
3. Rebase commands:
4. gitFlow COmmands:


Setting your Git username for every repository on your computer.  

Open Terminal.

Set a Git username:
```
UserName: 

$ git config --global user.name "Mona Lisa"
Confirm that you have set the Git username correctly:
Email: 

$ git config --global user.email "email@example.com"

```
```
To show username and email for globlly settings: 

$ git config --global user.name
Mona Lisa
$ git config --global user.email 
email@example.com

```

Setting your Git username and mail for a single repository
Open Terminal.

Setup Git username and mail :
```

Set UserName : 
$ cd <your local repository folder>
$ git config --local user.name "Mona Lisa"
Confirm that you have set the Git username correctly:

Set Email: 
$ git config --local user.email "email@example.com"

Show Local User: 
$ git config --local user.name
Mona Lisa

Show Local Email :

$ git config --local user.email 
email@example.com

```
### Delete all branches except master:
```
$ git branch | grep -v "master" | xargs git branch -D 
```
