from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.utils.translation import gettext_lazy as _


ADDRESSES = (
    ('', 'Выбери...'),
    ('Общежитие №1', 'Общежитие №1 (тимка)'),
    ('Общежитие №1', 'Общежитие №1 (тимка)'),
    ('Общежитие №3', 'Общежитие №3 (тимка)'),
    ('Общежитие №4', 'Общежитие №4 (тимка)'),
    ('Общежитие №5', 'Общежитие №5 (тимка)'),
    ('Общежитие №6', 'Общежитие №6 (тимка)'),
    ('Общежитие №7', 'Общежитие №7 (тимка)'),
    ('Общежитие №8', 'Общежитие №8 (тимка)'),
    ('Общежитие №9', 'Общежитие №9 (тимка)'),
    ('Общежитие №10', 'Общежитие №10 (тимка)'),
    ('Общежитие №11', 'Общежитие №11 (тимка)')
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(
        label="Имя"
    )
    last_name = forms.CharField(
        label="Фамилия"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        labels = {
            'username': _('Ссылка на телеграмм аккаунт (как логин)'),
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={'placeholder': 'Имя'})
    )
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(attrs={'placeholder': 'Фамилия'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': _('Ссылка на телеграмм аккаунт (как логин)'),
        }


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']


class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    address = forms.ChoiceField(choices=ADDRESSES)


# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import Profile
# from django.utils.translation import gettext_lazy as _
#
#
# ADDRESSES = (
#     ('', 'Выбери...'),
#     ('Общежитие №1', 'Общежитие №1 (тимка)'),
#     ('Общежитие №1', 'Общежитие №1 (тимка)'),
#     ('Общежитие №3', 'Общежитие №3 (тимка)'),
#     ('Общежитие №4', 'Общежитие №4 (тимка)'),
#     ('Общежитие №5', 'Общежитие №5 (тимка)'),
#     ('Общежитие №6', 'Общежитие №6 (тимка)'),
#     ('Общежитие №7', 'Общежитие №7 (тимка)'),
#     ('Общежитие №8', 'Общежитие №8 (тимка)'),
#     ('Общежитие №9', 'Общежитие №9 (тимка)'),
#     ('Общежитие №10', 'Общежитие №10 (тимка)'),
#     ('Общежитие №11', 'Общежитие №11 (тимка)')
# )
#
#
# class CustomAuthenticationForm(AuthenticationForm):
#     def __init__(self, request=None, *args, **kwargs):
#         super().__init__(request=None, *args, **kwargs)
#         self.fields['username'].label = 'Ссылка на телеграмм аккаунт (как логин)'
#         self.fields['password'].label = 'Пароль'
#
#
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
#         labels = {
#             'username': _('Ссылка на телеграмм аккаунт (как логин)'),
#             'first_name': _('Имя'),
#             'last_name': _('Фамилия'),
#         }
#
#
# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name']
#         labels = {
#             'username': _('Ссылка на телеграмм аккаунт (как логин)'),
#             'first_name': _('Имя'),
#             'last_name': _('Фамилия'),
#         }
#
#
# class ProfileUpdateForm(forms.ModelForm):
#     address = forms.ChoiceField(choices=ADDRESSES)
#
#     class Meta:
#         model = Profile
#         fields = ['image', 'address']
#         labels = {
#             'address': _('Адрес общежития'),
#         }
#
#
# class AddressForm(forms.Form):
#     email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#     password = forms.CharField(widget=forms.PasswordInput())
#     address_1 = forms.CharField(
#         label='Addre',
#         widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
#     )
#     address_2 = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
#     )
#     address = forms.ChoiceField(choices=ADDRESSES)
