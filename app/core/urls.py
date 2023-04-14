from core.views import HomePageView
from django.urls import path

app_name = "core"

urlpatterns = [
    path("", HomePageView.as_view()),
]
