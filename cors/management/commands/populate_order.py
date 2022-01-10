from random import randrange
from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time
from faker import Faker
from cors.models import Order, OrderItem


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        for _ in range(3):
            order = Order.objects.create(
                user_id=3,
                transaction_id=10,
                code="code",
                ambassador_email="b@gmail.com",
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                complete=True,
            )

            for _ in range(randrange(1, 5)):
                price = randrange(10, 100)
                quantity = randrange(1, 5)
                OrderItem.objects.create(
                    order_id=order.id,
                    product_title=faker.name(),
                    price=price,
                    quantity=quantity,
                    admin_revenue=0.9 * price * quantity,
                    ambassador_revenue=0.1 * price * quantity,
                )
