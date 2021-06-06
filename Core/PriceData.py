import requests
from Core.models import TokenData


def _get_price_json():

    url = "https://api.pancakeswap.info/api/tokens/0x3D29Aa78fB558F84112bbC48a84F371147A920C9"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    pancake_price = requests.get(url=url, headers=headers)
    try:
        pancake_price.raise_for_status()
        pancake_price = pancake_price.json()
        return pancake_price["data"]["price"]
    except:
        print("Problem while getting price from Pancake API...\n")
        return None


def update_dogefather_price():
    price = _get_price_json()
    if price is not None:
        try:
            dogefather_data = TokenData.objects.get(symbol='DOGEFATHER')
            dogefather_data.current_price = price
            dogefather_data.save(force_update=True)
            print("Updating...\n" + dogefather_data.symbol)
        except:
            print("Problem while updating price...\n")
            pass