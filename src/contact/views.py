from models import Contact
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    c = get_object_or_404(Contact, pk=1)
    return render_to_response('index.html', {'contact': c })
