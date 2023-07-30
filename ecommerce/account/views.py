from django.shortcuts import render, redirect
from django.template import ContextPopException

from . forms import CreateUserForm, LoginForm, UpdateUserForm

from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from .token import user_tokenizer_generate

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode                                              #decode and encode token generator


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

def register(request):                                                                                                  #registration process starts HERE, once done passed
                                                                                                                        #to email-verification.html
    form = CreateUserForm()

    if request.method =='POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user=form.save()

            user.is_active = False                                                                                      #by default newly registered accounts deactivated before verification

            user.save()

            current_site=get_current_site(request)

            subject = 'Account verification email'

            message = render_to_string('account/registration/email-verification.html',{                                 #adding token handling to email-verification, preparing
                                                                                                                        #to pass it into email-verification.html
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),
            })

            user.email_user(subject=subject,message=message)


            return redirect('email-verification-sent')                                                                  #once a form gets submitted, redirection to emaiil-verification-sent


    context ={'form':form}                                                                                              #passing in the form inside a context


    return render(request,'account/registration/register.html',context=context)

def email_verification(request,uidb64,token):                                                                           #pulling id from urls

    unique_id = force_str(urlsafe_base64_decode(uidb64))                                                                      #decoding user id
    user = User.objects.get(pk=unique_id)


    #IN CASE OF SUCCESS                                                                                                 #if user clicked on verification link

    if user and user_tokenizer_generate.check_token(user,token):

        user.is_active = True                                                                                           #activating user's account

        user.save()

        return redirect('email-verification-success')

    #IN CASE OF FAILURE

    else:

        return redirect('email-verification-failed')


def email_verification_sent(request):

    return render(request,'account/registration/email-verification-sent.html')


def email_verification_success(request):

    return render(request,'account/registration/email-verification-success.html')



def email_verification_failed(request):

    return render(request,'account/registration/email-verification-failed.html')



def my_login(request):

    form = LoginForm()

    if request.method =='POST':

        form = LoginForm(request,data=request.POST)

        if form.is_valid():

            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')


    context = {'form':form}

    return render(request,'account/my-login.html',context=context)


def user_logout(request):

    auth.logout(request)

    return redirect("store")

@login_required(login_url='my-login')
def dashboard(request):

    return render(request,'account/dashboard.html')

@login_required(login_url='my-login')
def profile_management(request):

    #Updating user's username and email

    if request.method =='POST':

        user_form=UpdateUserForm(request.POST,instance=request.user)                                                    #based on the currently signed in user

        if user_form.is_valid():

            user_form.save()

            return redirect('dashboard')

    user_form = UpdateUserForm(instance=request.user)                                                                   #updating a specific instance of user


    context ={'user_form':user_form}

    return render(request,'account/profile-management.html',context=context)



@login_required(login_url='my-login')
def delete_account(request):

    user = User.objects.get(id=request.user.id)

    if request.method =='POST':

        user.delete()

        return redirect('store')                                                                                        #users redirected to store after account deletion

    return render(request,'account/delete-account.html')






