from django.core.files.storage import default_storage
from django.http import Http404
from django.shortcuts import render, redirect
from functools import lru_cache
from math import ceil
from ..models import ExpertAnswer

perPage = 600

def realmain(request):
    return redirect('bird/?next=rooster,falcon')

def main(request, objname):
    if request.method == 'POST':
        biases = request.POST['biases']
        # record biases
        ExpertAnswer.objects.create(answer=biases, object=objname)
    if objname == 'over':
        return render(request, 'images/index.html', {'next': 'over', 'later': 'over', 'maxPage': 0, 'last': 'over'})
    imgs = images(objname)
    if imgs:
        maxPage = ceil(len(imgs) / perPage)
        next = request.GET.get('next', '').split(',', 1)
        if len(next) == 2:
            next, later = next
        elif next[0] == '':
            next = 'over'
            later = 'over'
        else:
            next = next[0]
            later = 'over'
        return render(request, 'images/index.html', {'next': next, 'later': later, 'maxPage': maxPage, 'last': objname})
    raise Http404("Imageset not found")

@lru_cache()
def images(objdata):
    return default_storage.listdir(f'Expert_Data/{objdata}')[1]

def pane(request, objname):
    imgs = images(objname)
    maxPage = ceil(len(imgs) / perPage)
    page = int(request.POST.get('page', '0'))
    imgUrls = []
    imgsToShow = imgs[page*perPage:(page+1)*perPage]
    imgUrls = [default_storage.url(f'Expert_Data/{objname}/{img}') for img in imgsToShow]
    return render(request, 'images/pane.html', {'images': imgUrls, 'page': page, 'maxPage': maxPage, 'last': objname})
