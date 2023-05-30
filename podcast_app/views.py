from django.shortcuts import render
from django.views import generic

from podcast_app import models

# Create your views here.
class PodcastReadView(generic.View):

    def get(self, request):
        return render(request, template_name='home.html', context={'podcasts': models.Podcast.objects.all()})