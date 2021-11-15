from django.shortcuts import render
from django.views import View


class AppSee(View):
    def get(self, request):
        return render(request, "base.html")
