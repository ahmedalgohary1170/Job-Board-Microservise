import os,django
from datetime import datetime
from django.utils.timezone import make_aware
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


import random
from faker import Faker
from posts.models import Post , PostLike , Comment

def generate_fake_posts(num=10):
    fake = Faker()
    for _ in range(num):
        title = fake.job()
        Post.objects.create(
            title = title,
            content = fake.paragraph(nb_sentences=10),
            puplish_at = make_aware(datetime(2024, 12, 15)),
            auther_id = random.randint(1,20) ,


        )


def generate_fake_post_likes(num=10):
    posts = Post.objects.all()
    for _ in range(num):
        PostLike.objects.create(
            user_id = random.randint(1,20) ,
            post = random.choice(posts)
        )


def generate_fake_cooments(num=10):
    posts = Post.objects.all()
    fake = Faker()
    for _ in range(num):
        Comment.objects.create(
            user_id = random.randint(1,20),
            post = random.choice(posts),
            content = fake.text(),
            comment_data = fake.date()
        )

generate_fake_posts(5)
generate_fake_post_likes(10)
generate_fake_cooments(10)