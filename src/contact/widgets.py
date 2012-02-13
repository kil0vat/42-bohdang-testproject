from django.forms.widgets import Input

class CalendarAJAXInput(Input):
    def __init__(self, attrs={}):
        self.input_type = 'hidden'
        super(CalendarAJAXInput, self).__init__(attrs)
