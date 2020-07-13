from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . import models
from .models import movie_list

from django.template import loader
def movie(request):
    mn = movie_list.objects.all()
    tempelate = loader.get_template('NewDemo/details.html')
    context ={
        'mn':mn,
    }
    return HttpResponse(tempelate.render(context,request))


def details(request, movie_id):
    try:
        movies = movie_list.objects.get(pk=movie_id)
    except movie_list.DoesNotExist:
        raise Http404('Movies not available')
    md = models.details.objects.get(pk=movie_id)
    return render(request, 'NewDemo/about.html', {'movies': movies,'md':md})

