from apscheduler.schedulers.background import BackgroundScheduler
from Core import PriceData


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(PriceData.update_dogefather_price, 'interval', minutes=5)
    scheduler.start()
