from .models import Post
from django.forms import ModelForm, TextInput
#
#
# class Form(ModelForm):
#     class Meta:
#         model = Orders
#         fields = ['title', 'price', 'deliver_price', 'photoid']

    # Файл еще дописывать и дописывать
# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'price', 'price_deliver', 'image']
#
#         widgets = {
#             'title': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder':'Название заказа'
#             }),
#             'price': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Стоимость товара'
#             }),
#             'price_deliver': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Стоимость доставки'
#             }),
#             'image': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Изображение'
#             })
#         }
