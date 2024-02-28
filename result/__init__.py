from django import template

register = template.Library()

from result.templatetags import bootstrap_filters