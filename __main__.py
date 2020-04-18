from telegram.ext import Updater, CommandHandler

import rates
import settings


def get_request_kwargs(proxy):
    return{
        'proxy_url': proxy,
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
    data = rates.get_rates_cached()
    output = "List of currencies: \n"
    for currency, rate in data.items():
        if rate != None:
            output += ("currency: %s rate: %s \n" % (currency, rate))
    update.message.reply_text(output)


def help(update, context):
    update.message.reply_text('Hi! \n /get \n /help')


def register_handlers(dp):
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("get", get))
    dp.add_handler(CommandHandler("help", help))


def routine(requestargs={}):
    updater = Updater(
        settings.TOKEN, request_kwargs=requestargs, use_context=True)
    register_handlers(updater.dispatcher)
    # Start the Bot
    updater.start_polling()
    updater.idle()


def main(currs=["BTC", "ETH"]):
    # if proxy list is present, use proxies
    if settings.PROXIES_LIST:
        for proxy in settings.PROXIES_LIST:
            try:
                print(proxy)
                routine(get_request_kwargs(proxy))
            except:
                print("connection error")
    else:
        routine()


if __name__ == "__main__":
    # execute only if run as a script
    main()
