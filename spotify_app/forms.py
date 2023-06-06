from django import forms
from .utils import get_all_genres


class PodcastChoiceForm(forms.Form):
    question_choices = (get_all_genres())

    if question_choices is not None:
        context = {'question_choices': question_choices}
    else:
        context = {}

    selected_choice = forms.MultipleChoiceField(label="Select genres of podcasts you like",
                                                choices=question_choices,
                                                widget=forms.CheckboxSelectMultiple)

    # question_choices = (
    #     ('1', 'True crime'),
    #     ('2', 'News commentary'),
    #     ('3', 'Society & Culture'),
    #     ('4', 'Parenting'),
    #     ('5', 'Language Learning'),
    #     ('6', 'Science'),
    #     ('7', 'Education'),
    #     ('8', 'History'),
    #     ('9', 'News'),
    #     ('10', 'Politics'),
    #     ('11', 'Comedy'),
    #     ('12', 'Philosophy'),
    #     ('13', 'Self Help'),
    #     ('14', 'Food'),
    #     ('15', 'Mental Health'),
    #     ('16', 'Health & Fitness'),
    #     ('17', 'Places & Travel'),
    #     ('18', 'Documentary'),
    #     ('19', 'Visual Arts'),
    #     ('20', 'Technology'),
    #     ('21', 'Nutrition'),
    #     ('22', 'Entrepreneurship'),
    #     ('23', 'Business'),
    #     ('24', 'Improv'),
    #     ('25', 'Personal Journals'),
    #     ('26', 'Soccer')
    # )


