from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import json

# Create your views here.


def home_view(request):

    context = {"none": ""}
    return render(request, "Core/index.html", context)
