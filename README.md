1.创建虚拟环境

2.改变端口并运行：python manage.py runserver 8080

3.初始化数据库：python manage.py migrate

4.创建管理员：python manage.py createsuperuser

5.新建数据表时：
    settings.py：INSTALLED_APPS-->添加'polls.apps.PollsConfig'  ---现在Django知道要包含该polls应用程序
    python manage.py makemigrations appname
    python manage.py sqlmigrate appname 0001
    python manage.py migrate appname
    
    
创建demo：django-admin startproject jiekou



a标签url网址：https://blog.csdn.net/heyue_99/article/details/56290018
    https://blog.csdn.net/weixin_42490528/article/details/84038102
    https://blog.csdn.net/qq_33867131/article/details/81949022
    