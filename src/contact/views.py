from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from models import Contact
from forms import ContactForm


def index(request):
    contact = get_object_or_404(Contact, pk=1)
    return render_to_response(
            'index.html', 
            {
                'contact': contact,
            },
            context_instance=RequestContext(request)
            )

@login_required
def edit_contact(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid(): 
            # Process the data in form.cleaned_data
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        contact = get_object_or_404(Contact, pk=1)
        initial = {}
        for field in contact._meta.fields:
            initial[field.name] = getattr(contact, field.name)
        form = ContactForm(
                initial=initial
                    )

    return render_to_response('edit_contact.html', {
        'form': form,
        },
        context_instance=RequestContext(request)
        )
