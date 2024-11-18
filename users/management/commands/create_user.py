from django.core.management import BaseCommand

from users.models import User
from django.contrib.auth.models import Group


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='user1@example.com')
        user.set_password('1234')
        user.is_active = True
        user.is_superuser = False
        user.is_staff = False
        users_group, created = Group.objects.get_or_create(name='Пользователи')
        user.groups.add(users_group)
        user.save()
        self.stdout.write(self.style.SUCCESS('Пользователь добавлен в группу "Пользователи"'))
