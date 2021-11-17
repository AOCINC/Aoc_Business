from django import template
from JobsApp.models import Job_Upload
register = template.Library()
import datetime

@register.filter(name='dayCount')
def dayCount():
    today =  datetime.datetime.now().date()
    return today
