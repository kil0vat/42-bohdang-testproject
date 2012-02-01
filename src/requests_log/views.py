from django.shortcuts import render_to_response
from django.template import RequestContext

from models import RequestsLogItem


def index(request):
    requests = RequestsLogItem.objects.all().order_by('time')
    return render_to_response(
            'requests_log.html', 
            {
                'requests': requests,
            },
            context_instance=RequestContext(request)
            )
