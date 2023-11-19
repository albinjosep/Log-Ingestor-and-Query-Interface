from django import forms
from log_ingestor import log_app


class LogSearchForm(forms.Form):
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)


class LogSearchForm(forms.Form):
    regex_search = forms.CharField(required=False)