from django.db import models

# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(verbose_name='Логин', max_length=50)
    firstname = models.CharField(verbose_name='Имя', max_length=50)
    lastname = models.CharField(verbose_name='Фамилия', max_length=50)
    surname = models.CharField(verbose_name='Отчество', max_length=50)
    user_email = models.EmailField(verbose_name='E-mail', unique=True)
