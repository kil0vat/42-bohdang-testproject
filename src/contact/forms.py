from django.forms import ModelForm, IntegerField, HiddenInput

from models import Person, Contact
from widgets import CalendarAJAXInput

class PersonForm(ModelForm):
    is_ajax_request = IntegerField(initial=0, widget=HiddenInput)
    class Meta:
        model = Person
        widgets = {
                'birth_date': CalendarAJAXInput(),
                }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('person',)

