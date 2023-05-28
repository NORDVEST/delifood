from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Ваша фотография', default='default.png', upload_to='profile_pics')
    address = models.CharField('Адрес общежития', blank=True, null=True, max_length=250)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 630 or img.width > 630:
            output_size = (630, 630)
            img.thumbnail(output_size)
            img.save(self.image.path)
