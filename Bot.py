#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import logging
import math

from random import random
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

token = "Input your telegram token"


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_text(f'Hi {user.first_name} {user.last_name}!')


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(f"you said {update.message.text}")

def quadratic(update: Update, _: CallbackContext) -> None:
    all_words = update.message.text.split(" ")
    terms = list(map(lambda x: int(x), all_words[1:]))
    a = terms[0]
    b = terms[1]
    c = terms[2]
    disc = (b**2) - (4*a*c)
    sol1 = (-b-math.sqrt(disc))/(2*a)
    sol2 = (-b+math.sqrt(disc))/(2*a)
    reply = f"Your roots are {sol1} and {sol2}"
    update.message.reply_text(reply)

def cat(update: Update, _: CallbackContext) -> None:
    number = int(random()*10000)
    url = f"https://cataas.com/cat?id={number}"
    update.message.reply_text(url)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("quadratic", quadratic))
    dispatcher.add_handler(CommandHandler("cat", cat))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

