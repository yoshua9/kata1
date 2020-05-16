from telegram.ext import Updater, CommandHandler

def main():
    #instanciar el updater
    updater = Updater(token=open("./Bot_Telegram/bot_token").read(), use_context=True)

    #Añadir un manejador del comando Start
    updater.dispatcher.add_handler(CommandHandler("start",start))

    #Añadir un manejador del comando Repite
    updater.dispatcher.add_handler(CommandHandler("repite",repite))

    #Añadir un manejador del comando Suma
    updater.dispatcher.add_handler(CommandHandler("suma",suma))

    #solicitamos notificaciones
    updater.start_polling()

    #Capturar señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text("Hola, soy un bot")

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    #args = [2,2] "Los args son de tipo str por defecto"
    resultado = int(context.args[0]) + int(context.args[1])
    resultado = str(resultado)
    update.message.reply_text("El resultado es: " + resultado)

main()
