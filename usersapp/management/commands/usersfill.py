from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from usersapp.models import CustomUser
import json
import os

JSON_PATH = 'usersapp/fixtures'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):

    def handle(self, *args, **options):
        if options['super']:
            super_user = get_user_model()
            try:
                super_user.objects.create_superuser('admin', 'admin@localhost', '12345')
                print("Суперпользователь успешно создан.")
            except Exception as e:
                print(f"Ошибка: {e} при создании суперпользователя")
        if options['users']:
            custom_users = load_from_json('custom_user')
            try:
                CustomUser.objects.all().delete()
                for custom_user in custom_users:
                    print(custom_user['fields'])
                    new_custom_user = CustomUser(**custom_user['fields'])
                    new_custom_user.save()
                print("Пользователи успешно созданы.")
            except Exception as e:
                print(f"Ошибка: {e} при создании пользователей")

    def add_arguments(self, parser):
        parser.add_argument(
            '-s',
            '--super',
            action='store_true',
            default=False,
            help='Создание суперпользователя'
        )
        parser.add_argument(
            '-u',
            '--users',
            action='store_true',
            default=False,
            help='Создание случайных пользователей'
        )