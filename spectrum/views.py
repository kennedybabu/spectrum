from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import InterestForm
from .models import Interest, Post,Comment
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    interests = Interest.objects.all()
    context = {
        'interests':interests
    }
    return render(request, 'spectrum/home.html', context)


def interest(request, pk):
    interest = Interest.objects.get(id=pk)
    posts = interest.post_set.all().order_by('-created')
    members = interest.members.all()

    if request.method == 'POST':
        post = Post.objects.create(
            user = request.user,
            interest = interest,
            body = request.POST.get('body')
        )

        return redirect('interest', pk=interest.id )
    context = {
     'interest':interest,  
      'members':members,
      'posts':posts
    }
    
    return render(request, 'spectrum/channel.html', context)


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
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

    context = {
        'page':page
    }
    return render(request, 'spectrum/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request): 
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'something went wrong during registration')

    context = {
        'form':form
    }
    return render(request, 'spectrum/login_register.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    # interests = user.interests_set.all()
    posts = user.post_set.all()
    context = {
        'user':user,
        # 'interests':interests,
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

    if request.user != interest.host:
        return HttpResponse('You are not allowed here!')

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

    if request.user != interest.host:
        return HttpResponse('You are not allowed to perform this action')

    if request.method == 'POST':
        interest.delete()
        return redirect('home')
    return render(request, 'spectrum/delete.html', {'obj':interest})



def joinInterest(request, pk):
    interest = Interest.objects.get(id=pk)
    interest.members.add(request.user)
    members = interest.members.all()

    context = {
        'interest':interest,
        'members':members
    }
    return render(request, 'spectrum/channel.html', context)


def quitInterest(request,pk):
    interest = Interest.objects.get(id=pk)
    interest.members.remove(request.user)
    members = interest.members.all()
    interests = Interest.objects.all()
    context = {
        'members':members,
        'interest':interest,
        'interests':interests
    }
    return render(request, 'spectrum/home.html', context)


def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.user != post.user:
        return HttpResponse('You are not allowed to perform this action')

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'spectrum/delete.html', {'obj':post})

    
