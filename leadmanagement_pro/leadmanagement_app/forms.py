from django import forms
from leadmanagement_app.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone_number', 'status', 'source']