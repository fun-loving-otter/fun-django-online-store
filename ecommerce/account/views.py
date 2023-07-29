from django.shortcuts import render, redirect

from . forms import CreateUserForm

from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from .token import user_tokenizer_generate

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode                                              #decode and encode token generator

def register(request):

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

            user.email_user(subject=subject,message=subject)


            return redirect('email-verification-sent')                                                                  #once a form gets submitted, redirection to emaiil-verification-sent


    context ={'form':form}                                                                                              #passing in the form inside a context


    return render(request,'account/registration/register.html',context=context)

def email_verification(request,uidb64,token):                                                                           #pulling id from urls

    uid = force_str(urlsafe_base64_decode(uidb64))                                                                      #decoding user id
    user = User.objects.get(pk=id)


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
