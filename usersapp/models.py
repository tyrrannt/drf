from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# class CustomUser(models.Model):
#     username = models.CharField(verbose_name='Логин', max_length=50)
#     firstname = models.CharField(verbose_name='Имя', max_length=50)
#     lastname = models.CharField(verbose_name='Фамилия', max_length=50)
#     surname = models.CharField(verbose_name='Отчество', max_length=50)
#     user_email = models.EmailField(verbose_name='E-mail', unique=True)

class CustomUser(AbstractUser):
    username = models.CharField(verbose_name='Логин', max_length=50, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=50, default='')
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    surname = models.CharField(verbose_name='Отчество', max_length=50)
    email = models.EmailField(verbose_name='E-mail', unique=True)
