from django.core.urlresolvers import reverse
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
    contact = get_object_or_404(Contact, pk=1)
    if request.method == 'POST': 
        form = ContactForm(
                request.POST, 
                instance=contact
                )
        if form.is_valid(): 
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect(reverse('index')) # Redirect after POST
    else:
        form = ContactForm(
                instance=contact
                )

    return render_to_response('edit_contact.html', {
        'form': form,
        },
        context_instance=RequestContext(request)
        )
