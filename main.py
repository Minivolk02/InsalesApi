import requests, schedule, time
import telegram
from telegram.ext import Updater, CommandHandler

bot = telegram.Bot(token='1003911757:AAG_yYI-nXPiOzdGTVVTQhHSShSQpIXl35g')
api_url = 'http://d5cce33618e5f3f75a766cac733f8a03:13f178f83cecbf1d56b384dab45477d9@myshop-4776-40.myinsales.ru/admin/orders.xml'

ORDERS = 0


def check_order():
    global ORDERS
    r = requests.get(api_url)
    orders = r.text.split('<order>')
    if len(orders) > ORDERS:
        ORDERS = len(orders)
        bot.send_message(587236480, f'У вас новый заказ(шучу, не у вас)\nВсего заказов {ORDERS}')


schedule.every().minute.do(check_order)

while True:
    schedule.run_pending()
    time.sleep(1)
