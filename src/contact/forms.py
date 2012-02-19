from django.forms import ModelForm, IntegerField, HiddenInput

from models import Contact
from widgets import CalendarAJAXInput

class ContactForm(ModelForm):
    is_ajax_request = IntegerField(initial=0, widget=HiddenInput)
    class Meta:
        model = Contact
        widgets = {
                'birth_date': CalendarAJAXInput(),
                }
