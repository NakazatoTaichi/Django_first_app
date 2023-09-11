from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.
class HomeView(View,LoginRequiredMixin):
    template_name = "index.html"