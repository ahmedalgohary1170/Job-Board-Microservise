import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from faker import Faker
from accounts.models import CustomUser

def generate_fake_users(num=10):
    fake = Faker()
    for _ in range(num):
        CustomUser.objects.create(
            email=fake.unique.email(),
            username=fake.user_name(),
            is_active=random.choice([True, False]),
            is_staff=random.choice([True, False]),
            date_joined=fake.date_time_this_year(),
        )

generate_fake_users()


