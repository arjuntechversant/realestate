from  django import forms
from django.contrib.auth.models import User
from .models import *


class RegisterUserForm(forms.ModelForm):
    name=forms.CharField(max_length=10)
    email=forms.EmailField(max_length=50)
    mobile_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}


    class Meta:
            model = UserProfile
            fields =['name', 'email', 'mobile_no','password']


class LoginUserForm(forms.Form):
        email = forms.EmailField(max_length=50)
        password = forms.CharField(widget=forms.PasswordInput)
        def __init__(self, *args, **kwargs):
            super(LoginUserForm, self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs = {'class': 'form-control'}

class AdPostingForm(forms.ModelForm):
    item_images=forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(AdPostingForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Item
        fields = '__all__'
        # exclude=('item_images',)

