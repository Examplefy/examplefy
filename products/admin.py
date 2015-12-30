from django.contrib import admin

# Register your models here.

from .models import Product, Example, Topic, Concept, Answer, Variation, ProductImage, Category, ProductFeatured

class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 0

class ProductAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'price']
	inlines = [
		VariationInline,
		ProductImageInline,
	]
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(Example)
admin.site.register(Topic)
admin.site.register(Concept)
admin.site.register(Answer)
# admin.site.register(Variation)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductFeatured)
