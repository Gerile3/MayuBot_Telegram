#!/usr/bin/env python3

from telegram.ext import Updater, CommandHandler
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
    functions = Funks()
    methods = [getattr(functions, m) for m in dir(functions) if not m.startswith('__')]
    names = [x for x in dir(Funks) if not x.startswith('__')]

    for i in range(len(methods)):
        dp.add_handler(CommandHandler(names[i], methods[i]))

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
