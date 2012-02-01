from models import Contact
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


def index(request):
    contact = get_object_or_404(Contact, pk=1)
    return render_to_response(
            'index.html', 
            {
                'contact': contact,
            },
            context_instance=RequestContext(request)
            )
