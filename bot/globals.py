import os, sys, logging, json

# ========== Logging =====================================================
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
# ========================================================================

# ========== Deployment ==================================================
def init_globals(bot_name):
    results = {}
    try:
        with open('bot/config.json') as json_file:
            config = json.load(json_file)
            results['TOKEN'] = config[bot_name]['token']
            results['URI'] = os.environ.get('MONGODB_URI', config[bot_name]['uri'])
            results['DATABASE_URL'] = os.environ.get('DATABASE_URL', config[bot_name]['database_url'])
            results['WEBHOOK_ADDRESS'] = config[bot_name]['webhook_address']
            results['ADDRESS'] = "0.0.0.0"
            results['PORT'] = int(os.environ.get('PORT', '8443'))
    except FileNotFoundError:
        print("I can't seem to find the `config.json` file that "
                "should be in the bot folder.")
        sys.exit()
    
    return results
# ========================================================================
