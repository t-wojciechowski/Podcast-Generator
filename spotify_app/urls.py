from django.contrib import admin
from django.urls import path
from . import views
from .forms import PodcastChoiceForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('podcast/list', views.podcast_list, name="podcast_list"),
    path('question/choice', views.question_choice, name='question_choice'),
    path('form/submit', views.question_form_submit, name='form_submit'),
]
