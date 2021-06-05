from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView #import TemplateView
from django.contrib.sitemaps.views import sitemap
from Core.views import (
    home_view,
    tesla_view
)

urlpatterns = [
    path('', home_view, name="home"),
    path('tesla', tesla_view, name='tesla'),
    path('sitemap.xml', sitemap,
         name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="Core/robots.txt", content_type="text/plain")),  #add the robots.txt file
]