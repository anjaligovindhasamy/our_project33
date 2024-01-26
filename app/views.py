from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.core.mail import send_mail


# Create your views here.
def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST'and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('registration',
                       'thank you ur registration is done',
                       'anjalig1710@gmail.com',
                       [MUFDO.email],
                       fail_silently=False)
            return HttpResponse('registration is done')
        else:
            return HttpResponse('registration is not done')
        
    return render(request,'registration.html',d)    