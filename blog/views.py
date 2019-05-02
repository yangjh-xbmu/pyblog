from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    entries = models.Entry.objects.all()
    return render(request, 'blog/index.html', locals())


def detail(request, blog_id):
    entry = models.Entry.objects.get(id=blog_id)
    entry.increate_visited()
    return render(request, 'blog/detail.html', locals())
