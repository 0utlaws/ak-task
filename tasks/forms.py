from django import forms

from tasks.models import (
    Task,
    Candidate,
    Recruiter,
    Grade
)


class GradeForm(forms.ModelForm):
    value = forms.ChoiceField(choices=Grade.RATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    task = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Task.objects.all())
    candidate = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                       queryset=Candidate.objects.all())
    recruiter = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                       queryset=Recruiter.objects.all())

    class Meta:
        model = Grade
        fields = ('value', 'task', 'candidate', 'recruiter')
