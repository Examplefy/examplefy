from django import template
register = template.Library()

from products.models import Product, THUMB_CHOICES

@register.filter 
def get_thumbnail(obj, arg):
	"""
	obj == Product Instance
	"""
	arg = arg.lower()
	if not isinstance(obj, Product):
		raise TypeError("Not a valid product model.")
	choices = dict(THUMB_CHOICES)
	if not choices.get(arg):
		raise TypeError("Not HD.")
	try:
		return obj.thumbnail_set.filter(type=arg).first().media.url
	except:
		return None