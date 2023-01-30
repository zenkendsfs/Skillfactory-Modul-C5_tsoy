import telebot
from uttils import ConvertionException , CryptoConverter ,TOKEN , keys
import requests

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands = ['start', 'help'])
def help (message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду следующим образом :\n - имя валюты :\n - в какую валюту перевести :\n - колличество нужной суммы валюты :\n Список валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text= '\n'.join((text, key, ))
    bot.reply_to(message, text) 
 

@bot.message_handler(content_types = 'text',)
def convert(message:telebot.types.Message):

        values = message.text.split(' ')  

        if len(values)<4:
           raise ConvertionException ('Слишком много параметров')
        
        quote, base, amount = message.text.split(' ')
        total_base = CryptoConverter.convert(quote,base,amount)
        
        text = f'Цена {amount}{quote} в {base} - {total_base}'
        
        bot.send_message(message.chat.id, text)

bot.polling()