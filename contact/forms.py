from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control input-sm'}), max_length=1000)