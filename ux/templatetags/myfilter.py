from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def kmgtbytes(value):
    unit = None
    units = ["TB", "GB", "MB", "KB", "Bytes"]
    num = value
    while num >= 1024:
        num /= 1024
        unit = units.pop()
    return "{} {}".format(num,unit)

@register.filter
def kilobytes(value):
    num = (value / 1024) / 1024
    return "{} KB".format( "{:,}".format(num))

@register.filter
def megabytes(value):
    num = ((value / 1024 ) / 1024) / 1024
    return "{} MB".format( "{:,}".format(num))

@register.filter
def to_utf8(value):
    return unicode(value)

@register.filter
def desc(value, arg):
    if not value:
        return ""
    vals = value.split('\n')
    for val in vals:
        if arg.upper() in val.upper():
           return val
    return ""