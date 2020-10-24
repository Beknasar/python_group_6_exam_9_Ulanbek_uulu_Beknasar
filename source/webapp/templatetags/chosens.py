from django import template

register = template.Library()


@register.filter
def chosen_by(obj, user):
    return obj.chosen_by(user)