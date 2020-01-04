from django.shortcuts import render
from django.views.generic import ListView
from .models import Slider

class Index(ListView):
    model = Slider
    template_name = "index.html"
