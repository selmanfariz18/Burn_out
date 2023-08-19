from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.




def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        #address = request.POST['address']
        email_id = request.POST['email']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request, 'Email is already taken')
                return redirect('register')
            else:
                # Create user and profile objects
                user = User.objects.create_user(username=username, password=password, email=email_id)
                user.save()
                messages.success(request, 'Account created successfully.')
                return render(request,'signin.html')
    return render(request,'register.html')

def signin(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request=request,username=username,password=password)
        if user is not None:
            login(request=request,user=user)
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.error(request,"Error in login")
            return HttpResponseRedirect(reverse("signin"))
    else:
        return render(request, 'signin.html')
    
def logout_user(request):
    logout(request)
    messages.success(request,"Logout Successfull!")
    #verification_code = "{:04d}".format(random.randint(0, 9999))
    #print(verification_code)
    return HttpResponseRedirect(reverse("signin"))



def home(request):
    return render(request,'base.html')