from django import forms
from .models import Post
from django.utils.translation import gettext_lazy as _
import datetime


weekdays = {0: 'Пн',
            1: 'Вт',
            2: 'Ср',
            3: 'Чт',
            4: 'Пт',
            5: 'Сб',
            6: 'Вс'}
month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
              'ноября', 'декабря']

DATET = (
    (f'{(datetime.datetime.now() + datetime.timedelta(days=0)).date()}', 'Сегодня'),
    (f'{(datetime.datetime.now() + datetime.timedelta(days=1)).date()}', 'Завтра'),
    (f'{(datetime.datetime.now() + datetime.timedelta(days=2)).date()}',
     f'{weekdays[(datetime.datetime.now() + datetime.timedelta(days=2)).weekday()]}, '
     f'{(datetime.datetime.now() + datetime.timedelta(days=2)).day}'
     f' {month_list[(datetime.datetime.now() + datetime.timedelta(days=2)).month - 1]}'),
    (f'{(datetime.datetime.now() + datetime.timedelta(days=3)).date()}',
     f'{weekdays[(datetime.datetime.now() + datetime.timedelta(days=3)).weekday()]}, '
     f'{(datetime.datetime.now() + datetime.timedelta(days=3)).day}'
     f' {month_list[(datetime.datetime.now() + datetime.timedelta(days=3)).month - 1]}'),
    (f'{(datetime.datetime.now() + datetime.timedelta(days=4)).date()}',
     f'{weekdays[(datetime.datetime.now() + datetime.timedelta(days=4)).weekday()]}, '
     f'{(datetime.datetime.now() + datetime.timedelta(days=4)).day}'
     f' {month_list[(datetime.datetime.now() + datetime.timedelta(days=4)).month - 1]}'),
    (f'{(datetime.datetime.now() + datetime.timedelta(days=5)).date()}',
     f'{weekdays[(datetime.datetime.now() + datetime.timedelta(days=5)).weekday()]}, '
     f'{(datetime.datetime.now() + datetime.timedelta(days=5)).day}'
     f' {month_list[(datetime.datetime.now() + datetime.timedelta(days=5)).month - 1]}'),
    (f'{(datetime.datetime.now() + datetime.timedelta(days=6)).date()}',
     f'{weekdays[(datetime.datetime.now() + datetime.timedelta(days=6)).weekday()]}, '
     f'{(datetime.datetime.now() + datetime.timedelta(days=6)).day}'
     f' {month_list[(datetime.datetime.now() + datetime.timedelta(days=6)).month - 1]}'),
)


class PostForm1(forms.ModelForm):
    mod = forms.CharField(
        label="Выбери мод",
        initial='Просто сэкономить',
        disabled=True,
        widget=forms.HiddenInput()
    )
    date_deliver = forms.ChoiceField(
        label="Дата ордера",
        choices=DATET
    )
    time_deliver = forms.TimeField(
        label="Время ордера",
        initial='17:30',
        widget=forms.NumberInput(attrs={'type': 'time'})
    )

    class Meta:
        model = Post
        fields = ['title', 'price', 'price_deliver', 'cnt_people', 'date_deliver', 'time_deliver', 'image', 'mod']
        # labels = {
        #     'username': _('Ссылка на телеграмм аккаунт (как логин)'),
        # }


class PostForm2(forms.ModelForm):
    mod = forms.CharField(
        label="Выбери мод",
        initial='Можно посидеть',
        disabled=True,
        widget=forms.HiddenInput()
    )
    date_deliver = forms.ChoiceField(
        label="Дата ордера",
        choices=DATET
    )
    time_deliver = forms.TimeField(
        label="Время ордера",
        initial='17:30',
        widget=forms.NumberInput(attrs={'type': 'time'})
    )

    class Meta:
        model = Post
        fields = ['title', 'price', 'price_deliver', 'cnt_people', 'date_deliver', 'time_deliver', 'image', 'mod']
        # labels = {
        #     'username': _('Ссылка на телеграмм аккаунт (как логин)'),
        # }


class PostForm3(forms.ModelForm):
    mod = forms.CharField(
        label="Выбери мод",
        initial='Тусовка по интересам',
        disabled=True,
        widget=forms.HiddenInput()
    )
    date_deliver = forms.ChoiceField(
        label="Дата ордера",
        choices=DATET
    )
    time_deliver = forms.TimeField(
        label="Время ордера",
        initial='17:30',
        widget=forms.NumberInput(attrs={'type': 'time'})
    )

    class Meta:
        model = Post
        fields = ['title', 'price', 'price_deliver', 'cnt_people', 'date_deliver', 'time_deliver', 'image', 'mod']
        # labels = {
        #     'username': _('Ссылка на телеграмм аккаунт (как логин)'),
        # }
