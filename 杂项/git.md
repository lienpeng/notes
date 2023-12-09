##### 1.1 基本命令

git stage  = git add
git diff --staged = git diff --cached

git stage好处
分批提交
git stage a.py c.py
git commit -m ""
git stage b.py
git commit -m ""
2、分阶段提交
// modify a.py
git stage a.py
// modify a.py
git commit -m "" 只会提交第一次的修改
3、文件快照，方便回退
git stage a.py
// modify a.py
git checkout -- a.py

git diff 当前工作区和stage区文件的差异
git diff --staged stage区和HEAD的文件差异
git diff HEAD 工作区和上次递交文件的差异

git status

git reset a.py 从stage区删除，不会影响工作区
git commit -a 跳过git stage  直接提交（不会作用于新建的文件）

git add后的撤销操作

git restore forcebot/pom.xml

##### 1.2 删除所有commit记录

1. 创建孤立分支，并切换到该分支：
`git checkout --orphan latest_branch`

2. 暂存所有文件：
`git add -A`

4. 提交所有更改：
`git commit -am "First Commit"`

5. 删除主分支 master：
`git branch -D master`

6. 重命名当前分支为 master：
`git branch -m master`

7. 强制推送本地分支：
`git push -f origin master`

