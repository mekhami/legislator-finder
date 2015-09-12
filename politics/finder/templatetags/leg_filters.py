from django import template

register = template.Library()


@register.filter(name='full_party')
def full_party(value):
    if value == "R":
        return "Republican"
    elif value == "D":
        return "Democrat"
    elif value == "I":
        return "Independent"
    else:
        return value
