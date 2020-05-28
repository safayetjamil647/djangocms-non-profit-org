from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from webmanager.models import *


# Create your views here.


def home(request):
    return render(request, 'webmanager/home.html')


def contact(request):
    return render(request, 'webmanager/contact.html')


def appeals(request):
    appeals = Appeal.objects.all()
    context = {'appeals': appeals}

    return render(request, 'webmanager/appeals.html', context)


def sponsor(request):
    sponsors = Sponsor.objects.all()
    context = {'sponsors': sponsors}
    return render(request, 'webmanager/sponsor.html', context)


def events(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'webmanager/events.html', context)


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'webmanager/blog.html', context)


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        "blog": blog,
    }
    return render(request, "webmanager/blog_detail.html", context)


def gallery(request):
    galleries = Gallery.objects.all()
    context = {'galleries': galleries}
    return render(request, 'webmanager/gallery.html', context)


def donation(request):
    return render(request, 'webmanager/donation.html')


def dashboard(request):
    return render(request, 'webmanager/dashboard.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'webmanager/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'webmanager/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
