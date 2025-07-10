import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("سلام! من سارا هستم. چه کمکی ازم برمیاد؟")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("دستورات:\n/start - شروع\n/help - کمک")

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"تو گفتی: {update.message.text}")

def main():
    # جایگزین کن با توکن خودت
    updater = Updater("7367637398:AAFmAdUeyrVqFP5AIHrVBXDyQUsao6DEn6Q", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
