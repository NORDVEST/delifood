from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Post(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    price_deliver = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    def save(self):
        super().save()

