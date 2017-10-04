from django import template


register = template.Library()


@register.simple_tag(name='ng')
def ng_tag(content):
    return "{{{{{0}}}}}".format(content)


@register.filter(name='ng', is_safe=True)
def ng_filter(content):
    return "{{{{{0}}}}}".format(content)
