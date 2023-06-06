from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from .utils import get_popular_podcasts
from .forms import PodcastChoiceForm

from spotify_app import models


# Create your views here.

def home(request):
    return render(request, "index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try other username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect('home')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request, "Passwords don't match")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-numeric")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created")


        return redirect('signin')

    return render(request, "signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {"fname": fname})
        else:
            messages.error(request, "Wrong details")
            return redirect('home')

    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')


def podcast_list(request):
    podcasts = get_popular_podcasts()

    if podcasts is not None:
        context = {'podcasts': podcasts}
    else:
        context = {}

    return render(request, 'podcast_list.html', context)


def question_choice(request):
    form = PodcastChoiceForm()
    return render(request, "question_choice.html", {'form': form})


# funkcja służy do obsługi przesłanych danych
def question_form_submit(request):
    if request.method == 'POST':
        form = PodcastChoiceForm(request.POST)
        if form.is_valid():
            selected_choice = form.cleaned_data['selected_choice']

            return redirect('success')
    else:
        form = PodcastChoiceForm()
    return render(request, 'index.html', {'form': form})








# class PodcastReadView(PermissionRequiredMixin, generic.View):
#     permission_required = 'podcasts.view_kurs'
#     def get(self, request):
#         return render(request, template_name='podcast_read.html', context={'podcasts': models.Podcast.objects.all()})


