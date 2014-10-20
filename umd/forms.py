from django import forms
from django.forms import ModelForm
from umd.models import URL   

class URLForm(ModelForm):
	class Meta:
		model = URL
		fields = "__all__" 