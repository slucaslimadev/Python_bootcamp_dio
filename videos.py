from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Eu sou um bot.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Coloque seu token aqui
    token = '7402551614:AAErI1USj01Wqltt9HrdC3DdPlsIUandIlk'
    
    # Cria o Updater e passa o token do seu bot
    updater = Updater(token)

    # Obtém o dispatcher para registrar os handlers
    dispatcher = updater.dispatcher

    # Registrar os handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Iniciar o bot
    updater.start_polling()

    # Executa até que você pare o script
    updater.idle()

if __name__ == '__main__':
    main()
