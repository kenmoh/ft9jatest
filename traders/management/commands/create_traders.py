from typing import Any
from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from datetime import timedelta
from traders.models import User

"""
This is a management command to generate 10 random users and add to mongodb database.
"""


class Command(BaseCommand):
    number_of_traders = 10

    help = "Generate random Traders"

    def handle(self, *args: Any, **options: Any):
        for i in range(self.number_of_traders):
            username = f'Trader{i + 1}'
            password = 'password' + username
            user = User.objects.create(username=username, balance=100.00)
            user.set_password(password)
            user.save()

            self.stdout.write(self.style.SUCCESS(
                f'Users {user.username} created successfully.'))
