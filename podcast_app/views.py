from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from podcast_app import models
from podcast_app import forms

# Create your views here.
class PodcastReadView(generic.View):
    # permission_required = 'kursy.view_kurs'
    def get(self, request):
        return render(request, template_name='registration/home.html', context={'podcasts': models.Podcast.objects.all()})


class PodcastCreateView(LoginRequiredMixin, generic.FormView):
    template_name = 'podcast_form.html'
    form_class = forms.PodcastForm
    success_url = reverse_lazy('podcast_home')

    def form_valid(self, form):
        result = super().form_valid(form)
        data = form.cleaned_data

        models.Podcast.objects.create( # tu okreslamy co ma sie wydarzyc jesli wszystko dobrze się wykona
            title=data['title'],
            description=data['description']
        )

        return result


class UserCreateView(generic.CreateView):
    template_name = 'user_form.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('podcast_home')