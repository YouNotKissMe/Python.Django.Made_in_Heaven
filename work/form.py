from .models import Publication
from django.forms import ModelForm


class PublictionForm(ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'category','author', 'synopsis', 'file')

