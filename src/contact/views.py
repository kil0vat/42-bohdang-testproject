import json

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from models import Contact
from forms import ContactForm, PersonForm

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
        form_person = PersonForm(
                request.POST, 
                request.FILES,
                prefix='person',
                instance=contact.person
                )
        form_contact = ContactForm(
                request.POST, 
                request.FILES,
                prefix='contact',
                instance=contact
                )
        is_ajax_request = form_person.data.get('person-is_ajax_request',0)
        if form_person.is_valid() and form_contact.is_valid(): 
            # Process the data in form.cleaned_data
            form_person.save()
            form_contact.save()
            response = json.dumps({
                'success': True,
                'html': 'Data is succesfully updated.'
                })
        else:
            html = form_person.errors.as_ul() + form_contact.errors.as_ul()
            response = json.dumps({'success': False, 'html': html})

        if is_ajax_request:
            return HttpResponse(response, content_type="application/javascript")
        else:
            if form_person.is_valid() and form_contact.is_valid(): 
                return HttpResponseRedirect(reverse('index')) # Redirect after POST
    else:
        form_contact = ContactForm(
                prefix="contact", instance=contact
                )
        form_person = PersonForm(
                prefix="person", instance=contact.person
                )

    return render_to_response('edit_contact.html', {
        'contact': contact,
        'form_contact': form_contact,
        'form_person': form_person,
        },
        context_instance=RequestContext(request)
        )
