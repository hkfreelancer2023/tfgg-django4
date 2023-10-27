#from django.shortcuts import render

# Create your views in Core App

from django.views import generic

class HomeView(generic.TemplateView):
	"""
    Website home page for core app.

    **Template:**

    :template:`core/index.html`
    """
	template_name = "index.html"
	
    