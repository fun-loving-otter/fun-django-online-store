from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username','email','password1','password2']                                                           #based on the user model

    def __init__(self,*args, **kwargs):                                                                                 #gaining access to the above attributes
        super(CreateUserForm,self).__init__(*args,**kwargs)                                                             #inheriting userform and all of its fields

#Email validation
    def clean_email(self):

        email=self.cleaed_data.get("email")

        if User.objects.filter(email=email).exists():                                                                   #checking if an email address already exists in a database
            raise forms.validationError('This email is ivalid')

        if len(email>=350):
            raise forms.ValidationError('Your email address is too long')