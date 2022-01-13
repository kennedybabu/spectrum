from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import InterestForm
from .models import Interest, Post,Comment


# Create your views here.
def home(request):
    interests = Interest.objects.all()
    context = {
        'interests':interests
    }
    return render(request, 'spectrum/home.html', context)


def interest(request, pk):
    interest = Interest.objects.get(id=pk)
    context = {
     'interest':interest   
    }
    
    return render(request, 'spectrum/channel.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')

    context = {}
    return render(request, 'spectrum/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    interests = user.interests_set.all()
    posts = user.post_set.all()
    context = {
        'user':user,
        'interests':interests,
        'posts':posts,
    }
    return render(request, 'spectrum/profile.html', context)


def createInterest(request):
    form = InterestForm()
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            # interest.host = request.user
            interest.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'spectrum/channel_form.html', context)


def updateInterest(request, pk):
    interest = Interest.objects.get(id=pk)
    form = InterestForm(instance=interest)

    if request.method == 'POST':
        form = InterestForm(request.POST, instance=interest)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'spectrum/channel_form.html', context)


def deleteInterest(request, pk):
    interest = Interest.objects.get(id=pk)

    if request.method == 'POST':
        interest.delete()
        return redirect('home')
    return render(request, 'spectrum/delete.html', {'obj':interest})
    
