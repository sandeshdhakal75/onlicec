from django import forms
from .models import Public


class PublicForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    crime_location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    complain_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_crime= forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    time_of_crime = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    complain_description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Public
        fields = ['full_name','crime_location','contact_number','date_of_crime','time_of_crime','gender','complain_description','evidence']
