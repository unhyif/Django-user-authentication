from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField("닉네임", max_length=20)
    tel = models.CharField("연락처", max_length=15)