from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from pages.forms import *
from pages.models import *

# Create your views here.
def Inicio (request): 
    return render(request, "core/index.html") 

class AboutUs (LoginRequiredMixin,TemplateView): 
    template_name = 'core/about_us.html'

@login_required
def Blog (request):
    pages = Page.objects.all()
    return render(request, "core/blog.html", {'pages': pages})