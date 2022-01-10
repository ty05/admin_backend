from random import randrange
from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time
from faker import Faker
from cors.models import User
from django_redis import get_redis_connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        con = get_redis_connection("default")

        ambassadors = User.objects.filter(is_ambassador=True)

        for ambassador in ambassadors:
            con.zadd("ranking", {ambassador.name: float(ambassador.revenue)})
