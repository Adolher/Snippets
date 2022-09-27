# git workflow basics
[see for detailed information](https://git-scm.com/book/de/v2)
___
## configure git
|  | command | description |
| --- | --- | --- |
| - | git config --global core.editor "\<editor> | set default editor [commands](https://git-scm.com/book/de/v2/Anhang-C%3A-Git-Kommandos-Setup-und-Konfiguration#ch_core_editor)
| - | git config --global --edit | opens a user-specific configuration file |
| - | git config --local --edit | opens a repository-specific configuration file |
| - | git config --system --edit | opens a system-level configuration file |
| - | git config --global user.email "\<email-add> | save E-Mail-Address of current user |
| - | git config --global user.name "\<name> | save the name of the current user |
___
## create and push a git repository
| step | command | description |
| --- | --- | --- |
| 0 | | move to projects directory or create one |
| 1 | git init |  |
| 2 | git add <file(s)> | git add . -> git add all files in directory |
| 3 | git commit -m "initial commit" |  |
| 4 | git branch -M main | rename master-branch to main-branch |
| 5 | git remote add origin \<remote-repository-link> | e.g. https://github.com/Adolher/test.git |
| 6 | git push -u origin main |  |
___
## clone a repository
| step | command | description |
| --- | --- | --- |
| 0 | | move to directory where project should be in |
| 1 | git clone  \<remote-repository-link> | e.g. https://github.com/Adolher/test.git |
___
## work on a repository (single)
| step | command | description |
| --- | --- | --- |
| 0 | | move to projects directory |
| 1 | git pull | get the actual repository to working directory |
| (1-1) | git fetch | get the actual repository to staging area |
| (1-2) | git checkout | update files in working directory to match the staging area |
| 2 | | work on your project |
| (2.5) | git diff | show differences between working directory and staging area |
| 3 | git status | show changes between working directory and staging area |
| 4-1 | git add \<file> | add new files to staging area |
| 4-2 | git commit -m "\<message> | commit (move) changes to staging area |
| (4) | git commit -a | commit changes to staging area (without new files) |
| 6 | git push -u origin main | move changes to remote repository |

## branch a repository
