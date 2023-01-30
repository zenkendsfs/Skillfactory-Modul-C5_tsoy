import json
from config import keys 
import requests
import telebot

TOKEN = '5912521454:AAGfYegJrXzmiz-0InUFANaiyABkZYm9fGA'
keys =  {
    'доллар': 'USD',
    'биткоин': 'BTC',
    'эфирион': 'ETH'
}  

bot = telebot.TeleBot(TOKEN)

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str , base: str , amount: str): 
        
        if quote==base:
           raise ConvertionException(f'Невозможно перевести одинаковую валюту {base}')
    
        try:
           quote_ticker=keys[quote]
        except KeyError:
           raise ConvertionException (f'не удалось обработать{quote}')

        try:
           base_ticker=keys[base]
        except KeyError:
           raise ConvertionException (f'не удалось обработать{base}')
    
        try:
          amount=float[amount]
        except ValueError:
            raise ConvertionException (f'не удалось обработать колличество{amount}')
        

        @bot.message_handler(content_types=['text'])
        def converter(message: telebot.types.Message):
          base, quote, amount = message.text.split(' ')
          r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
          resp = json.loads(r.content)
          new_price = resp['rates'][quote] * float(amount)
          bot.reply_to(message, f"Цена {amount} {base} в {quote} : {new_price}")