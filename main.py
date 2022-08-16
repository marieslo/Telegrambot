
import telebot
from telebot import types
from config import TOKEN
from extensions import Converter, APIException


def create_markup(base = None):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    buttons = []
    for val in exchanges.keys():
        if val != base:
            buttons.append(types.KeyboardButton(val.capitalize()))

    markup.add(*buttons)
    return  markup


bot = telebot.TeleBot(TOKEN)

keys = {
    'доллар США': "USD",
    'евро': "EUR",
    'российский рубль': "RUB"
}

@bot.message_handler(commands=["start", "help"])
def start(message: telebot.types.Message):
    text = "Напишите через пробел в следующем порядке: \n- название валюты \n- в какую валюту перевести \n- количество переводимой валюты. \nСписок доступных валют можно увидеть по команде: /values"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Неверное количество параметров!')

        answer = Convertor.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)

bot.polling()