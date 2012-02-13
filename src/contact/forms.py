from django.forms import ModelForm

from models import Contact
from widgets import CalendarAJAXInput

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
                'birth_date': CalendarAJAXInput(),
                }
