from django.db import models

# Create your models here.


class Birthday(models.Model):
    state = models.CharField(max_length=10)  # 01阴历 02阳历
    year = models.CharField(max_length=4)  # 年
    mouth = models.CharField(max_length=2)  # 月
    day = models.CharField(max_length=2)  # 日  初几

