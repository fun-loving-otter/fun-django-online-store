from django.shortcuts import render, redirect

from . forms import CreateUserForm

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

def email_verification(request):

    pass


def email_verification_sent(request):

    pass


def email_verification_success(request):

    pass


def email_verification_failed(request):

    pass