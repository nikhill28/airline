from django.contrib.auth import authenticate,login,logout


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated: # request has user attribute #user attriute has is_authenticateed attribute
        return HttpResponseRedirect(reverse("login"))    

#two method for login, 1.GET-show mw the log in form  2.POST-subit the data to the login form as well

def login(request):
    if request.method=="POST":
        username= request.POST["username"]
        password= request.POST["password"] # get the password from the field in the request,pOST inside of password
       
        user=authenticate(request,username=username,password=password)
        if user is not None: #authentiaction succesfully
            login(request,user)
            return HttpResponseRedirect(reverse('index')) #authentiaction succesfully
        else:
            return render(request,'users/login.html',{
                "message":"invalid id/pass"
            })
    return render(request,"users/login.html")


def logout(request):
    return render(request,"users/logout.html")