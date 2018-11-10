# gitCommands
Trying to pull files from my Github repository: “refusing to merge unrelated histories”  

 Solved by this command: 

```
$ git pull origin master --allow-unrelated-histories

```

Setting your Git username for every repository on your computer.  

Open Terminal.

Set a Git username:
```
git config --global user.name "Mona Lisa"
Confirm that you have set the Git username correctly:
```
```
git config --global user.name
Mona Lisa
```

Setting your Git username for a single repository
Open Terminal.

Set a Git username:
```
$ cd <your local repository folder>
$ git config user.name "Mona Lisa"
Confirm that you have set the Git username correctly:

$ git config user.name
Mona Lisa

```
