from django import template

register = template.Library()

@register.filter
def availability_label(item):
    if not item.available:
        return f"{item.name} (Coming Soon)"
    return item.name