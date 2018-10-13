1.创建虚拟环境

2.改变端口并运行：python manage.py runserver 8080

3.初始化数据库：python manage.py migrate

4.创建管理员：python manage.py createsuperuser

<<<<<<< HEAD
django


http://47.93.28.78:8888/admin
=======
5.新建数据表时：
    settings.py：INSTALLED_APPS-->添加'polls.apps.PollsConfig'  ---现在Django知道要包含该polls应用程序
    python manage.py makemigrations polls
    python manage.py sqlmigrate polls 0001
>>>>>>> fca42b5d6c500e161d1ecebd3f0752a665627a6a
