import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from models import RequestsLogItem


def index(request):
    requests = RequestsLogItem.objects.all().order_by('time')[:10]
    return render_to_response(
            'requests_log.html', 
            {
                'requests': requests,
            },
            context_instance=RequestContext(request)
            )

def update_priority(request):
    response = json.dumps({'success': False})
    if request.method == 'POST': 
        if request.is_ajax():
            id = request.POST['id']
            priority = request.POST['priority']
            try:
                i = RequestsLogItem.objects.get(id=id)
                i.priority = priority
                i.save()
                response = json.dumps({'success': True, 'id': id, 'priority': priority})
            except:
                response = json.dumps({'success': False})
    return HttpResponse(response, content_type="application/javascript")
