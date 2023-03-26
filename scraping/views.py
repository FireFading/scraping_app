from core.models import News
from django.shortcuts import render
from django.views import generic


class HomePageView(generic.ListView):
    template_name = "home.html"
    context_object_name = "articles"

    def get_queryset(self):
        return News.objects.all()
