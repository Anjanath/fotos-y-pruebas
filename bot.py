import telebot
import random
import time

bot = telebot.TeleBot("1477201095:AAG-Cixn38nTU9soGlkKT9ylHwWCsczMtSU")

time = time.asctime()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Iniciado.")

@bot.message_handler(commands=['hola', 'adios'])
def send_message(message):
    bot.reply_to(message, "Mensaje de prueba.")

@bot.message_handler(commands=['hora', 'fecha'])
def fecha(message):
    bot.reply_to(message, time)

@bot.message_handler(func=lambda message: True, content_types=['audio'])
def default_command3(message):
    bot.reply_to(message, "Soy sordo, no te escucho.")

@bot.message_handler(func=lambda message: True, content_types=['sticker'])
def default_command(message):
    bot.reply_to(message, "Bonita pegatina.")

@bot.message_handler(regexp='Un conejo')
def send_message(message):
    bot.send_photo(message.chat.id, ("https://raw.githubusercontent.com/Anjanath/fotos-y-cosas/main/conejo.jpg"))

@bot.message_handler(regexp='cerdo' and 'bonito')
def send_message(message):
    bot.send_photo(message.chat.id, photo=open("/home/xavier/Documentos/cerdo.jpg", "rb"))

@bot.message_handler(regexp='cerdo' and 'feo')
def send_message(message):
    bot.send_photo(message.chat.id, photo=open("/home/xavier/Documentos/cerdofeo.jpg", "rb"))

@bot.message_handler(commands=['numero_aleatorio'])
def send_message(message):
    bot.reply_to(message, random.randrange(10))

@bot.message_handler(commands=['cerdo_aleatoria'])
def foto_aleatoria(message):
    numero = random.randint(1, 2)
    if numero == 1:
             bot.send_photo(message.chat.id, photo=open("/home/xavier/Documentos/cerdo.jpg", "rb"))
    elif numero == 2:
             bot.send_photo(message.chat.id, photo=open("/home/xavier/Documentos/cerdofeo.jpg", "rb"))

@bot.message_handler(commands=['casino'])
def send_message(message):
    bot.reply_to(message, '🎲')

bot.polling()
