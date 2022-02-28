
## yeh new file banaye
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxLengthValidator
from django.db.models.constraints import UniqueConstraint
from .models import User

class SignUpForm(forms.ModelForm):
    testfor = (
        ('option', 'Select_Option'),
        ('afterten', 'After10th'),
        ('aftertwelve', 'After12th'),
    )

    typeof = (
        ('option', 'Select_Option'),
        ('parent', 'Parent'),
        ('guardian', 'Guardian'),
        ('student', 'Student'),
    )
    
    
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name=forms.CharField()
    aadhar_no=forms.CharField()
    mobile = forms.CharField()
    user_type = forms.ChoiceField(choices = typeof, initial="Select_Option")
    test_after = forms.ChoiceField(choices = testfor,initial='Select_Option')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','aadhar_no','mobile', 'user_type','test_after','password', 'confirm_password']


class LoginForm(forms.Form):
    
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        fields = ['email', 'password']



