from django import forms
from django.contrib.flatpages.models import FlatPage
from django.forms.models import ModelForm
from tinymce.widgets import TinyMCE
from notes.models import Interview

class InterviewForm(ModelForm):
    company = forms.CharField(max_length=50)
    position = forms.CharField(max_length=50)
    date = forms.DateField()
    description = forms.CharField(max_length=2000, \
        widget=TinyMCE(attrs={'rows':15,'cols':80}))

    question = forms.CharField(max_length=2000, \
        widget=TinyMCE(attrs={'rows':10,'cols':80}))
    answer = forms.CharField(max_length=2000, \
        widget=TinyMCE(attrs={'rows':10,'cols':80}))

    class Meta:
        model = FlatPage
        exclude = ('profile',)
        fields = ('company', 'position', 'date', 'description')
