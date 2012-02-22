from django.forms.widgets import Input

class CalendarAJAXInput(Input):
    def __init__(self, attrs={}):
        self.input_type = 'hidden'
        super(CalendarAJAXInput, self).__init__(attrs)

    class Media:
        css = {
                'all': ('/js/jdpicker_1.0.3/jdpicker.css'),
                }
        js = ('/js/jdpicker_1.0.3/jquery.jdpicker.js',)
        images = (
                '/js/jdpicker_1.0.3/images/bg_hover.png',
                '/js/jdpicker_1.0.3/images/bg_selectable.png',
                '/js/jdpicker_1.0.3/images/bg_selected.png',
                )
