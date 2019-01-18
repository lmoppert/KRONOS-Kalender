from django import template


register = template.Library()


@register.filter
def get_holiday(value, arg):
    """Get the holiday name from a given date"""
    return arg.get(value)
