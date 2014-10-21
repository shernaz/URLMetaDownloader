from django import forms
from django.forms import ModelForm
from umd.models import URL   

class URLForm(forms.ModelForm):
	url = forms.CharField(help_text="Please enter a url:")
	title = forms.CharField(help_text="Please enter title:")
	meta_desc = forms.CharField(help_text="Please enter meta description:")
	meta_keyword = forms.CharField(help_text="Please enter meta keyword:")
	class Meta:
		model = URL
		fields = ['url', 'title', 'meta_desc', 'meta_keyword']
		
		
class URLModifyForm(forms.ModelForm):
	url = forms.CharField(help_text="Url")
	title = forms.CharField(help_text="Title")
	meta_desc = forms.CharField(help_text="Meta description")
	meta_keyword = forms.CharField(help_text="Meta keyword")
	class Meta:
		model = URL
		fields = ['url', 'title', 'meta_desc', 'meta_keyword']