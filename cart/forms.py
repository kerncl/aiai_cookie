from datetime import date
from django import forms
from django.core.exceptions import ValidationError


class CartForm(forms.Form):
    start = forms.DateField()
    end = forms.DateField()

    # todo: looks like is for models, step to get it is through Profile._meta.fields[4].clean function
    # to_python -> validate -> clean_<field> -> clean
    # to_python: Take raw value turn into python obj (str)
    # validate: fields-specific validation on the data
    # clearn_<field>: place that we can customize our validate function
    # clearn: addition clean that needs to be done on the form as a whole

    # Form
    # full_clean -> _clean_fields, _clean_form, _post_clean
    # _clean_fields: called all clean_<field>
    # _clean_form: get cleaned_data
    # _post_clean: for Model
    def clean_start(self):
        value = self.cleaned_data['start']
        if value < date.today():
            # Ensure date is today or later
            raise ValidationError("How can we delivery it before today ?")

        # Change format to YYYY-MM-DD
        return value.strftime("%Y-%m-%d")

    def clean_end(self):
        value = self.cleaned_data['end']
        return value.strftime("%Y-%m-%d")
