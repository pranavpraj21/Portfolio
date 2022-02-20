from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .models import Project,reviewed
from .forms import reviewform
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def signupuser(request):
    if request.method=='GET':
        return render(request,'portfolio/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'portfolio/signupuser.html',{'form':UserCreationForm(),'error':'username already exists'})
        else:
            return render(request,'portfolio/signupuser.html',{'form':UserCreationForm(),'error':'password did not match'})

def loginuser(request):
    if request.method=='GET':
        return render(request,'portfolio/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'portfolio/loginuser.html',{'form':AuthenticationForm(),'error':'Username/Password does not exist, Please try again'})
        else:
            login(request,user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method =='POST':
        logout(request)
        return redirect('home')


def reviews(request):
    all_reviews = reviewed.objects.all()
    return render(request, 'portfolio/all_reviews.html', {'all_reviews':all_reviews})

@login_required
def createreview(request):
    if request.method=='GET':
        return render(request,'portfolio/createreview.html',{'form':reviewform()})
    else:
        try:
            form = reviewform(request.POST)
            newreview = form.save(commit=False)# We are not saving it now, cause we will add the user, then save
            newreview.Name = request.user
            newreview.save()
            return redirect('reviews')
        except ValueError:
            return render(request,'portfolio/createreview.html',{'form':reviewform(),'error':'Bad Data, Please try again'})
