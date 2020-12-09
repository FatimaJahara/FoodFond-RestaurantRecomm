from django import forms

class RecommendForm(forms.Form):
	userpreference = forms.CharField(max_length=200)
	