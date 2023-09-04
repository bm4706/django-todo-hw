from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile = models.TextField(null=True, blank=True)
    # 좋아요 기능추가 + Many~를 넣으면 얘가 브릿지테이블을 따로 만들어서 db에 만듬
    like_todos = models.ManyToManyField("todo.Todo", related_name="like_users")
    follow = models.ManyToManyField("self", symmetrical=False, related_name="followers")