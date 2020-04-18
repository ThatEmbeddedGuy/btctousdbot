import http.client, sys, getopt, requests, json
import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown
from concurrent.futures import ThreadPoolExecutor

import rates, settings


#http://spys.one/proxys/DE/
REQUEST_KWARGS={
    'proxy_url':settings.PROXY_URL,
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'assert_hostname': 'False',
        'cert_reqs': 'CERT_NONE'
        # 'username': 'user',
        # 'password': 'password'
    }
}

def start(update, context):
    update.message.reply_text('Hi! \n /get \n /help')

def get(update, context):
    data = rates.get_rates_concurrent()
    output="List of currencies: \n"
    for currency, rate in data.items():
         if rate != None:
           output+=("curency: %s rate: %s \n" %(currency,rate))
    update.message.reply_text(output)

def help(update, context):
    update.message.reply_text('Hi! \n /get \n /help')

def register_handlers(dp):
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("get", get))
    dp.add_handler(CommandHandler("help", help))

def main(currs = ["BTC","ETH"] ):
    updater = Updater(settings.TOKEN,request_kwargs=REQUEST_KWARGS, use_context=True)

    # Get the dispatcher to register handlers
    register_handlers(updater.dispatcher)

    # Start the Bot
    updater.start_polling()

    updater.idle()
  

if __name__ == "__main__":
    # execute only if run as a script
    main()
