import datetime
from django.utils import dateformat
from django import template

register = template.Library()


@register.filter()  # Штука, которая регистрирует фильтр
def addDays(days):
   newDate = datetime.date.today() + datetime.timedelta(days=days)
   return newDate

