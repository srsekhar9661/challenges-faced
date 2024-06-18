from django import forms
from .models import Template, Narrative


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'content', 'parent_template']
        

class NarrativeForm(forms.ModelForm):
    class Meta:
        model = Narrative
        fields = ['subject', 'age', 'content']

        