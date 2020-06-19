from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import TemplateView


def index_view(request, *args, **kwargs):
    if request.user.id is None:
        return render(request, "guest.html")
    else:
        return render(request,"user.html")

class IndexView(TemplateView):
    template_name = "guest.html"
