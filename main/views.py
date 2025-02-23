import pathlib

from django.http import HttpResponse
from django.shortcuts import render
from visits.models import *

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    path = request.path
    querysets_path = PageVisit.objects.filter(path = path)
    total_visits = PageVisit.objects.count()

    page_title = "Home Page"
    context = {
        "page_title": page_title,
        "querysets_path": querysets_path,
        "querysets_path_count": querysets_path.count(),
        "total_visits": total_visits,
    }
    html_template = 'home.html'
    page_visits = PageVisit.objects.create(path=path)
    return render(request, html_template, context)