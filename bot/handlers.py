from telegram.ext import CommandHandler, MessageHandler, Filters

from bot.base import pm_start, error_handler

# ============ private message handlers ==========================================
pm_start_handler = CommandHandler('start', pm_start)
# ================================================================================
