from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Customer



class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    #First_name = forms.CharField( max_length=100 )
    #Last_name = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = [ 'email', 'username','password1', 'password2']

class AddRecords(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    
