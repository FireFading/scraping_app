from core.models import News
from django.views.generic import ListView


class HomePageView(ListView):
    template_name = "home.html"
    context_object_name = "articles"

    def get_queryset(self):
        return News.objects.all()
