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
        fields = (
                'bio',
                'birth_date',
                'last_name',
                'first_name',
                'photo',
                )

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = (
                'other_contacts', 
                'skype', 
                'jabber', 
                'email',
                )
        exclude = ('person',)

