from django import forms


class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, help_text="Put Name")
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)
