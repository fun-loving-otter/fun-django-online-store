from django.shortcuts import render, redirect

from . forms import CreateUserForm
def register(request):

    form = CreateUserForm()

    if request.method =='POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('store')                                                           #if the form was submitted correctly we will be redirected to the store page

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