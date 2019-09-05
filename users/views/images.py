from django.core.files.storage import default_storage
from django.http import Http404
from django.shortcuts import render
from functools import lru_cache
from math import ceil
from ..models import ExpertAnswer

def main(request, objname):
    if images(objname):
        return render(request, 'images/index.html')
    raise Http404("Imageset not found")

@lru_cache()
def images(objdata):
    return default_storage.listdir(f'Expert_Data/{objdata}')[1][:300]

def pane(request, objname):
    perPage = 100
    imgs = images(objname)
    maxPage = ceil(len(imgs) / perPage)
    page = int(request.POST.get('page', '0'))

    imgUrls = []
    if page < maxPage:
        imgsToShow = imgs[page*perPage:(page+1)*perPage]
        imgUrls = [default_storage.url(f'Expert_Data/{objname}/{img}') for img in imgsToShow]
    elif page == maxPage:
        biases = request.POST['biases']
        # record biases
        #ExpertAnswer.objects.create(answer=biases)
    return render(request, 'images/pane.html', {'images': imgUrls, 'page': page, 'maxPage': maxPage})
