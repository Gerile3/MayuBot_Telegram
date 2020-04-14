#!/usr/bin/env python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from funks import Funks

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main(api_key):
    """Start the bot."""
    updater = Updater(api_key, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", Funks.start))
    dp.add_handler(CommandHandler("help", Funks.help))
    dp.add_handler(CommandHandler("mayu", Funks.mayu))
    dp.add_handler(CommandHandler("location", Funks.location))
    dp.add_handler(CommandHandler("meme", Funks.meme))
    dp.add_handler(CommandHandler("coin", Funks.coin))
    dp.add_handler(CommandHandler("weather", Funks.weather))
    dp.add_handler(CommandHandler("horos", Funks.horos))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, Funks.echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


if __name__ == '__main__':
    print("i am running!")
    with open("auth2.yaml", 'r') as f:
        api_key = f.readline()
    main(api_key)
