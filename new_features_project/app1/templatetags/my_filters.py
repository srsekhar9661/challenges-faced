from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplies the value by the argument."""
    return value * arg

@register.filter
def to_uppercase(value):
    """Converts a string to Uppercase."""
    return value.upper()

@register.filter
def to_lower(value, *args):
    return value.lower()

@register.filter
def number(value, arg):
    return f"{value} -- {len(value)} - {arg.split('-')} "