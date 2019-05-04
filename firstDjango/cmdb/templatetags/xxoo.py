__author__ = "那位先生Beer"
from django import template
register=template.Library()

@register.simple_tag
def qkq(a,b):
    return a+b