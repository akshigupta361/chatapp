from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    import math, random
    if 'submit' in request.POST:
        otp=random.randint(1000,9999)
        print(otp)
        return render(request,'login.html',{'otp':otp})
    elif 'otp_submit' in request.POST:
        if request.POST['old_otp']==request.POST['otp']:
            message="Input Username"
            return render(request,'login.html',{'message':message})
        else:
            message="Wrong OTP"
            otp=random.randint(1000,9999)
            print(otp)
            return render(request,'login.html',{'otp':otp})
    elif 'user_submit' in request.POST:
        msg= 'You are logged in as '
        return HttpResponse(msg + request.POST['username'])
    return render(request,'login.html',{})

    

