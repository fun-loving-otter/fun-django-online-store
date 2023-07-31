from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput,TextInput


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username','email','password1','password2']                                                           #based on the user model

    def __init__(self,*args, **kwargs):                                                                                 #gaining access to the above attributes
        super(CreateUserForm,self).__init__(*args,**kwargs)                                                             #inheriting userform and all of its fields


        self.fields['email'].required=True                                                                              #making email a required field in the forms

#Email validation
    def clean_email(self):

        email=self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():                                                                   #checking if an email address already exists in a database
            raise forms.ValidationError('This email is invalid')

        if len(email) >= 350:
            raise forms.ValidationError('Your email address is too long')

        return email

# Log in

class LoginForm(AuthenticationForm):

    username=forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#Update username and email form

class UpdateUserForm(forms.ModelForm):

    password=None                                                                                                       #not updating the password

    class Meta:                                                                                                         #based on the user model

        model= User

        fields=['username','email']
        exclude = ['password1','password1']                                                                             #not making use of the passwords


    def __init__(self,*args, **kwargs):                                                                                 #gaining access to the above attributes
        super(UpdateUserForm,self).__init__(*args,**kwargs)


        self.fields['email'].required=True                                                                              #email address required when updating username





    def clean_email(self):

        email=self.cleaned_data.get("email")

        if User.objects.filter(email=email).eclude(pk=self.instance.pk).exists():                                       #checking if an email address already exists in a database
                                                                                                                        #user can update an username without updating his email address
            raise forms.ValidationError('This email is invalid')

        if len(email) >= 350:
            raise forms.ValidationError('Your email address is too long')

        return email