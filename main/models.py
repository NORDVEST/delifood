from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    price_deliver = models.FloatField()
    image = models.ImageField(upload_to='order_pics/')
    date_deliver = models.DateField(default=timezone.now)
    time_deliver = models.TimeField(default=timezone.now)
    cnt_people = models.IntegerField(default=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self):
        super().save()