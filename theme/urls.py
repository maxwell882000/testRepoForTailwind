from django.urls import path

from theme.views import AppSee

urlpatterns = [
    path("home/", AppSee.as_view())
]
