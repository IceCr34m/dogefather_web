from django.shortcuts import render
import requests
from dogefather_web.config import current_site_url
from Core.models import TokenData

# Create your views here.

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
    dogefather_data = TokenData.objects.get(symbol='DOGEFATHER')

    pancake_price = dogefather_data.current_price
    float_price = float(pancake_price)
    num_zeros = get_num_of_zeros(float_price)
    zeros = "0." + "0" * num_zeros
    price_suffix = pancake_price.split(zeros)[1][:11 - num_zeros]

    market_cap = str(round(float(dogefather_data.market_cap)))
    price = {"prefix": zeros,
             "suffix":  price_suffix,
             "market_cap": market_cap}

    web_site_url = {'url': current_site_url}

    # contruct context and render
    context = {"price": price,
               "site_url": web_site_url}
    return render(request, "Core/index.html", context)


def tesla_view(request):

    context = {"none": ""}
    return render(request, "Core/tesla.html", context)
