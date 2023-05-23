from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Название ордера", max_length=120, help_text='Введите текст поста')

    price = models.FloatField("Стоимость всей еды", default=0)
    price_deliver = models.FloatField("Стоимость доставки", default=0)
    date_deliver = models.DateField("Дата ордера", default=timezone.now)
    time_deliver = models.TimeField("Время ордера", default='17:30:00')
    cnt_people = models.IntegerField("Количество людей", default=2, help_text='Минимум 2, включая вас')

    image = models.ImageField(
        'Картинка',
        upload_to='posts_pics/',
        blank=True,
        null=True
    )

    mod = models.CharField('Мод ордера', blank=True, null=True, max_length=250)  # default='Просто сэкономить'

    class Meta:
        ordering = ('-date_posted',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 1280 or img.width > 1280:
            output_size = (1280, 1280)
            img.thumbnail(output_size)
            img.save(self.image.path)



# def get_image_filename(instance, filename):
#     id = instance.post.id
#     return "post_pics/%s" % (id)


# class Images(models.Model):
#     post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')
#
#     def save(self):
#         super().save()
#
#         img = Image.open(self.image.path)
#
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
