from django.template import Library

register = Library()

def multiply(id_atributo):
    return str(id_atributo * 65536)

register.filter("multiply", multiply)