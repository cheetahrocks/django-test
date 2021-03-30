from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
from appTwo.forms import NewUser

def v1(request):
    # return HttpResponse("<em>HI there</em>")
    return render(request, 'appTwo/index.html')
# Create your views here.

def users(request):
    f = NewUser()
    if request.method == 'POST':
        f = NewUser(request.POST)
        if f.is_valid():
            f.save(commit=True)  # saving the form data and commiting to the models
            return v1(request)
        else:
            print("Error -- Form invalid")

    return render(request, 'appTwo/users.html', {'form':f})


def help(request):
    d1 = { 'temp_var1': 'HELP PAGE'}
    return render(request, 'appTwo/help.html', context=d1)
    # variable temp_var1 outputs values passddto context as a dict
