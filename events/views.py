from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader

from .models import Event


def index(request):
    all_events = Event.objects.all()
    template = loader.get_template('events/index.html')
    context = {
        'all_events': all_events,
    }
    return HttpResponse(template.render(context, request))
