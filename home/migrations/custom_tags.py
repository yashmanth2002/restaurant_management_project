from django import template
import datetime

def current_year():
    return datetime.datetime.now().year