from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from projects.models import Project


def index(request):
    return render(request, "home/home.html")


def contact(request):
    return render(request, "home/contact.html")


def about(request):
    return render(request, "home/about.html")


class SearchView(generic.ListView):
    template_name = "projects/project_list.html"

    def get_queryset(self):
        param = self.request.GET.get("param")
        projects = Project.objects.filter(title__icontains=param)
        self.extra_context = {"mode": "search"}
        return projects
