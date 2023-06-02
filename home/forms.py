from django.forms import ModelForm
from . import models


class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
