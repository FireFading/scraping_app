from django.shortcuts import render
from django.views import generic


class HomePageView(generic.ListView):
    template_name = 'home.html'