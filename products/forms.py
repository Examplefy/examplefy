from .models import Variation, Product
from django import forms
from django.forms.models import modelformset_factory
from django.utils.text import slugify
from django.contrib import messages 

class VariationInventoryForm(forms.ModelForm):
	class Meta:
		model = Variation
		fields = [
		"price",
		"sale_price",
		"inventory",
		"active",
		]
VariationInventoryFormSet = modelformset_factory(Variation, form=VariationInventoryForm, extra=0)
PUBLISH_CHOICES = (
	("publish", "Publish"),
	("draft", "Draft"), 
)
from .models import Variation, Category



class ProductFilterForm(forms.Form):
	# q = forms.CharField(label='Search', required=False)
	category_id = forms.ModelMultipleChoiceField(
		label='Category',
		queryset=Category.objects.all(), 
		widget=forms.CheckboxSelectMultiple, 
		required=False)
	
	# max_price = forms.DecimalField(decimal_places=2, max_digits=12, required=False)
	# min_price = forms.DecimalField(decimal_places=2, max_digits=12, required=False)

class ProductModelForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = [
		"title",
		"description",
		"media",
		"categories",
		]
		widgets = {
			"description": forms.Textarea(
				attrs={
					"placeholder": "Description..."
				}
			),
			"title": forms.TextInput(
				attrs={
					"placeholder": "Question..."
				}
			),	
			"categories": forms.CheckboxSelectMultiple(
				attrs={
					"id": "topic_group"
				}
			),
		}
	def clean(self, *args, **kwargs):
		cleaned_data = super(ProductModelForm, self).clean(*args, **kwargs)
		# title = cleaned_data.get("title")
		# slug = slugify(title)
		# qs = Product.objects.filter(slug=slug).exists()
		# if qs:
		# 	raise forms.ValidationError("Unique question is required. Please submit a unique question title.")
		return cleaned_data

	def clean_title(self):
		title = self.cleaned_data.get("title")
		if len(title) > 0:
			return title
		else: 
			raise forms.ValidationError("Title must not be blank.")
	def clean_media(self):
		media = self.cleaned_data.get("media")
		if media is not None:
			return media
		else: 
			raise forms.ValidationError("Please upload a question image.")
	def clean_category(self):
		categories = self.cleaned_data.get("categories")
		if categories is not None:
			return categories
		else: 
			raise forms.ValidationError("Please select a question category.")

	# def clean_desc(self):
	# 	desc = self.cleaned_data.get("description")
	# 	if len(desc) > 3:
	# 		return desc
	# 	else: 
	# 		raise forms.ValidationError("Description must not be blank.")
