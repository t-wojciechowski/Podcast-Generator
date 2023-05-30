from django import forms

from podcast_app import models


class PodcastForm(forms.ModelForm):
    class Meta:
        model = models.Podcast
        fields = '__all__'
