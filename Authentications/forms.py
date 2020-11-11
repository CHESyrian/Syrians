from django import forms

class Register_Form(forms.Form):
    First_Name       = forms.CharField(max_length=16)
    Last_Name        = forms.CharField(max_length=16)
    User_Name        = forms.CharField(max_length=16)
    Email            = forms.EmailField()
    Birthday         = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Password         = forms.CharField(max_length=64, widget=forms.PasswordInput())
    Confirm_Password = forms.CharField(max_length=64, widget=forms.PasswordInput())