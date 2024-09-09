import os 
from flask import Flask

app = Flask(__name__)
from markupsafe import escape

@app.route("/")
def  helloWorld():
     print ("hello bro")
     return f'https://render-flask-8xdc.onrender.com/name'
     print ("hii bro ")
     return helloworld()
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text) 


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7042973932:AAGBtpQD1qgIByt4_-AOasvNG3mpPH_CMiY")>

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))










if __name__ == '__main__':
        port = os.environ.get('PORT', 5000)
        app.run(host='0.0.0.0', port=port)
