from django import forms

from datetime import *

from tablefor2 import *


DEPARTMENTS = (
    ('--', 'Select a Department'),
    ('Engineering', 'Engineering'),
    ('General & Administrative', 'General & Administrative'),
    ('Marketing', 'Marketing'),
    ('Success', 'Success')
)

LOCATIONS = (
    ('--', 'Select a Location'),
    ('San Francisco', 'San Francisco'),
    ('New York', 'New York'),
    ('Seattle', 'Seattle'),
    ('Lehi', 'Lehi'),
    ('Other', 'Other')
)

TIMEZONES = (
    ('--', 'Select your timezone by closest city'),
    ('EST (New York)', 'US/Eastern'),
    ('CST (Chicago)', 'US/Central'),
    ('MST (Denver, Lehi)', 'US/Mountain'),
    ('PST (San Francisco, Seattle)', 'US/Pacific'),
    ('BST (London)', 'Europe/London'),
    ('CEST (Barcelona, Madrid, Paris, Amsterdam)', 'Europe/Amsterdam'),
)

BOOLEANS = (
    ('--', 'Select a Choice'),
    ('Yes', 'Yes'),
    ('No', 'No')
)

FREQUENCY = (
    # ('--', 'Select a Frequency'),
    ('Once a week', 'Once a week'),
    # ('Once every other week', 'Once every other week'),
    # ('Once a month', 'Once a month')
)


class ProfileForm(forms.Form):
    preferred_name = forms.CharField(max_length=50)
    department = forms.ChoiceField(choices=DEPARTMENTS)
    location = forms.ChoiceField(choices=LOCATIONS)
    timezone = forms.ChoiceField(choices=TIMEZONES, help_text='Choose the closest city in your timezone')
    google_hangout = forms.ChoiceField(choices=BOOLEANS, help_text='If you are not matched with someone in your area, would you be willing to Google Hangout?')
    frequency = forms.ChoiceField(choices=FREQUENCY, help_text='How often do you want to participate?')
    date_entered_mixpanel = forms.DateField(help_text='(MM/DD/YYYY or YYYY-MM-DD)')

    def clean_department(self):
        department = self.cleaned_data.get('department')
        if department == '--':
            raise forms.ValidationError('Please select your department.')
        return department

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if location == '--':
            raise forms.ValidationError('Please select your location.')
        return location

    def clean_timezone(self):
        timezone = self.cleaned_data.get('timezone')
        if timezone == '--':
            raise forms.ValidationError('Please select the closest city in your timezone.')
        return timezone

    def clean_google_hangout(self):
        google_hangout = self.cleaned_data.get('google_hangout')
        if google_hangout == '--':
            raise forms.ValidationError('Please select your Google Hangout preference.')
        return google_hangout

    def clean_frequency(self):
        frequency = self.cleaned_data.get('frequency')
        if frequency == '--':
            raise forms.ValidationError('Please select your frequency to participate.')
        return frequency

    def clean_date_entered_mixpanel(self):
        date_entered_mixpanel = self.cleaned_data.get('date_entered_mixpanel')
        if date_entered_mixpanel > date.today():
            raise forms.ValidationError("Please enter a valid Mixpanel start time! (You started in the future?)")
        return date_entered_mixpanel


class AvailabilityForm(forms.Form):
    time_available = forms.DateTimeField(help_text='(MM/DD/YYYY HH:MM (military time) )')

    def clean_time_available(self):
        time_available = self.cleaned_data.get('time_available')
        return time_available
