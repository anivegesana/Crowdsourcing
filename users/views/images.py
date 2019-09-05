from django.core.files.storage import default_storage
from django.shortcuts import render

def main(request):
    return render(request, 'images/index.html')

def pane(request):
    objdata = "rooster"
    imgs = default_storage.listdir(f'Expert_Data/{objdata}')[1]
    imgsToShow = imgs[:50]
    imgUrls = [default_storage.url(f'Expert_Data/{objdata}/{img}') for img in imgsToShow]
    return render(request, 'images/pane.html', {'images': imgUrls})

def answers(request):
    return render(request, 'images/answers.html')
