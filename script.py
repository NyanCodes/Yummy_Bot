from typing import Final
import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN: Final = '7297857683:AAHQ4mR7cE4q3Fx_D7cLXfTQD2B_xczpLQw'
BOT_USERNAME: Final = '@DeliFoodie'

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
   await update.message.reply_text("Hello, Welcome to Delicia")

async def help(update, context: ContextTypes.DEFAULT_TYPE) -> None: 
    await update.message.reply_text (
    """
/start -> Welcome to Channel 
/menu  -> Food Menu 
/help  -> This particular Message 
    """ 
    )

async def shout_out(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Enter the vaild command")

def main() -> None: 
    # Create App
    application = Application.builder().token(TOKEN).build()

    # On different Commands
    application.add_handler(CommandHandler("/start", start))
    application.add_handler(CommandHandler("/help", help ))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shout_out))

    # Run the bot until user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES) 

if __name__ == "__main__":
    main()