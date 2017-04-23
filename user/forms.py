from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        #print(model.email,model.first_name,model.password,model.username)
        fields = ['username','email','password'] 

