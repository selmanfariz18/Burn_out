from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import PomodoroSession

# Create your views here.



#sign up form reciever
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


#signin form reciever
def signin(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request=request,username=username,password=password)
        if user is not None:
            login(request=request,user=user)
            return HttpResponseRedirect(reverse("user_page"))
        else:
            messages.error(request,"Error in login")
            return HttpResponseRedirect(reverse("signin"))
    else:
        return render(request, 'signin.html')


#logout function
def logout_user(request):
    logout(request)
    messages.success(request,"Logout Successfull!")
    #verification_code = "{:04d}".format(random.randint(0, 9999))
    #print(verification_code)
    return HttpResponseRedirect(reverse("signin"))

#user home page renders from here
@login_required
def user_page(request):
    user_sessions = PomodoroSession.objects.filter(user=request.user)
    return render(request, 'user_page.html', {'user_sessions': user_sessions})

#pomodora strating 
@login_required
def start_pomodoro(request):
    if request.method == 'POST':
        session = PomodoroSession.objects.create(user=request.user, start_time=datetime.now(), is_active=True)
        return JsonResponse({'session_id': session.id})
    return JsonResponse({'error': 'Invalid request'})

#pomodora stoping
@login_required
def stop_pomodoro(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        try:
            session = PomodoroSession.objects.get(id=session_id)
            session.end_time = datetime.now()
            session.is_active = False
            session.save()
            return JsonResponse({'message': 'Pomodoro session stopped successfully'})
        except PomodoroSession.DoesNotExist:
            return JsonResponse({'error': 'Session not found'})
    return JsonResponse({'error': 'Invalid request'})