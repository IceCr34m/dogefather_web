from django.shortcuts import render
import requests
from dogefather_web.config import current_site_url
from django.http import HttpResponseRedirect
import json

# Create your views here.
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def get_num_of_zeros(num):
    if not num:
        return 0
    current_num = abs(num)
    num_of_zeros = -1

    while not (current_num//1):
        current_num *= 10
        num_of_zeros +=1

    return num_of_zeros


def home_view(request):
    # Get price and format it
    pancake_price = requests.get('https://api.pancakeswap.info/api/tokens/0x3D29Aa78fB558F84112bbC48a84F371147A920C9',
                         headers=HEADERS)
    pancake_price = pancake_price.json()
    pancake_price = pancake_price["data"]["price"]
    float_price = float(pancake_price)
    num_zeros = get_num_of_zeros(float_price)
    zeros = "0." + "0" * num_zeros
    price_suffix = pancake_price.split(zeros)[1][:11 - num_zeros]
    price = {"prefix": zeros,
             'suffix':  price_suffix}
    web_site_url = {'url': current_site_url}

    # contruct context and render
    context = {"price": price,
               "site_url": web_site_url}
    return render(request, "Core/index.html", context)


def tesla_view(request):

    context = {"none": ""}
    return render(request, "Core/tesla.html", context)
