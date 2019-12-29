from telegram import ParseMode

from bot.globals import logger

def pm_start(update, context):
    """Send welcome message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)

    message = ("Hi, I'm `NFbb`, and I'm here to help you! 🤖" + "\n\n" +
               "I'll be collecting reports submitted to me via private message, " +
               "send these to Smart's databases, and share them to registered " +
               "groupchats!" + "\n\n")

    # if user.id in REPORTERS:
    #     message += "To *send a report*, do a /report." + "\n"
    # else:
    #     message += "To *register as a user*, do a /register." + "\n"

    # if user.id in ADMINS:
    #     message += "To *register a group chat*, go to that chat and do a /register\_gc." + "\n"

    message += "To see my full list of capabilities, do a /help."

    # if (user.id in USERS) and (user.id not in ADMINS):
    #     message += ("\n\n" + "You'll need to request from an admin to register a groupchat to " +
    #                 "receive finished reports.")

    update.message.reply_text(
        text = message,
        parse_mode = ParseMode.MARKDOWN
    )


def error_handler(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    # user = update.effective_user
    # for sa in SUPERADMINS:
    #     context.bot.send_message(
    #         chat_id = sa,
    #         text = ("Heya! Our user <a href='tg://user?id={}'>{}</a> -- while " +
    #                 "doing a /{} -- got this error:" + "\n\n" +
    #                 "<pre>{}</pre>" + "\n\n" +
    #                 "I'm sending this now to the superadmins.").format(
    #                     user.id,
    #                     user.full_name,
    #                     context.chat_data.get('mode'),
    #                     context.error
    #                 ),
    #         parse_mode = ParseMode.HTML
    #     )

