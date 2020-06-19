# 作业2

本次作业所需文件都在assignments/assignment02文件夹。此文件夹下是一个最简单的Django项目。
你的任务是让这个项目能在本地运行起来，并完成一个小任务。

## 熟悉 virtualenv 和 pip

virtualenv 和 pip 是在python开发过程中必不可少的工具，你这次的任务就是要熟悉这两个工具。
这里是一个关于 virtualenv 最简单的教程：https://www.liaoxuefeng.com/wiki/1016959663602400/1019273143120480
这里是关于 pip 的简单教程：https://www.runoob.com/w3cnote/python-pip-install-usage.html

你的第一个任务，是创建一个虚拟环境，并在其中使用pip安装好Django 2.2


## 本地运行项目

一旦你正确安装好 Django，则，进入目录：assignments/assignment02，也就是本文件所在的目录，运行：

```shell script
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

以上三行，会创建本地数据库，并创建一个超级管理员用户。请记住你的用户名和密码。

```shell script
python manage.py runserver
```

你就能在本地访问到运行起来的django站点。

## 熟悉Django

1. 打开浏览器，访问 http://localhost:8000/admin/ 查看django的后台管理界面。
1. 访问 http://localhost:8000/index.html 弄清楚这个页面是从哪里来的。
1. 修改代码，让此页面的内容，随访问者是否登录而发生变化。已登录的人看到的是templates/user.html里的内容；
未登录者看到的是templates/guest.html里的内容。
1. 重点查看 assignment02/settings.py, assignment02/urls.py, frontpage/urls.py, frontpage/views.py 。
对这四个文件里的每一行代码，你必须要知道它是什么意思，起什么作用，能不能删除，删除后有什么后果。


**修改后的代码，放入你们自己的handin分支。6月18日晚提交。**