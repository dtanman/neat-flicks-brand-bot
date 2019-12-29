from telegram.ext import Updater
import sys

from bot.globals import init_globals
from bot.handlers import pm_start_handler, error_handler

def main():
    # Updater object to represent the bot
    updater = Updater(config['TOKEN'], use_context=True)

    # get the dispatcher to register handlers
    dp = updater.dispatcher

    # add the two handlers
    dp.add_handler(pm_start_handler)
    # gc_nested_handler

    # error handler
    dp.add_error_handler(error_handler)
    
    if sys.argv[1]=='polling':
        updater.start_polling()
        print('==== POLLING NOW RUNNING ====')

    elif sys.argv[1]=='heroku':
        updater.start_webhook(listen=config['ADDRESS'], port=config['PORT'], url_path=config['TOKEN'])
        updater.bot.set_webhook(config['WEBHOOK_ADDRESS']+config['TOKEN'])
        print('==== WEBHOOK NOW RUNNING, EXPECTING HEROKU ====')
    
    # run the bot until a ctrl-c. Think of this as a while loop.
    updater.idle()


if __name__=='__main__':
    if len(sys.argv) < 3:
        print('==========================================')
        print('Please run as `python app.py [how] [who]`')
        print('[how]: "polling" or "heroku"')
        print('[who]: "nfbb" or "johnny"')
        print('==========================================')
        sys.exit()
    deployment = sys.argv[1]
    bot_name = sys.argv[2]

    print('initializing global variables...')
    config = init_globals(bot_name)
    print('initialized global variables')

    print('starting main...')
    main()
