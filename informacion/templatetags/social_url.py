from django.template import Library

register = Library()


@register.simple_tag()
def facebook_url():
    return "https://www.facebook.com/zralei/"
