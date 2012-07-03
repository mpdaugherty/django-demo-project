from django.http import HttpResponse
from django.shortcuts import render_to_response

from daily_quote import get_quote

def home(req):
    return HttpResponse(get_quote())

def home_with_template(req):
    context = {
        'quote': get_quote(),
    }
    return render_to_response('home.django', context)
