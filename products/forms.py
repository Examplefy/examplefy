from .models import Variation, Product
from django import forms
from django.forms.models import modelformset_factory

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

class ProductAddForm(forms.Form):
	title = forms.CharField(label='', widget=forms.TextInput(
			attrs={
			"placeholder": "Question...",
		}))
	description = forms.CharField(label='', widget=forms.Textarea(
			attrs={
			"placeholder": "Description...",
		}))
	# price = forms.DecimalField()
	#publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=True)
	def clean_title(self):
		title = self.cleaned_data.get("title")
		if len(title) > 3:
			return title
		else: 
			raise forms.ValidationError("Title must not be blank.")
	def clean_desc(self):
		desc = self.cleaned_data.get("description")
		if len(desc) > 3:
			return desc
		else: 
			raise forms.ValidationError("Description must not be blank.")

class ProductModelForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = [
		"title",
		"description",
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
			)
		}
	def clean_title(self):
		title = self.cleaned_data.get("title")
		if len(title) > 0:
			return title
		else: 
			raise forms.ValidationError("Title must not be blank.")
	def clean_desc(self):
		desc = self.cleaned_data.get("description")
		if len(desc) > 3:
			return desc
		else: 
			raise forms.ValidationError("Description must not be blank.")
