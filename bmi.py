import telebot
from telebot import types

bot = telebot.TeleBot('       ')

name = ''
age = 0
rost = 0
we = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Отправьте Боту 'Привет'  ")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет' or message.text == 'привет':
        bot.send_message(message.from_user.id, 'Здравствуйте! Как Вас зовут?')
        bot.register_next_step_handler(message, bname)


def bname(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, name + ', какой у Вас рост?\nНапример: 1.60')
    bot.register_next_step_handler(message, brost)


def brost(message):
    global rost
    try:
        rost = float(message.text)
        bot.send_message(message.from_user.id, name + ', какой у Вас вес?')
        bot.register_next_step_handler(message, bwe)
    except Exception:
        bot.send_message(message.from_user.id, name + ', какой у Вас рост?\nНапример: 1.60')
        bot.register_next_step_handler(message, brost)


def bwe(message):
    global we
    try:
        we = float(message.text)
        bmi = int(we) / float(rost) ** 2
        bmi = round(bmi, 1)

        if bmi < 18.5:
            bot.send_message(message.from_user.id, name+', индекс вашего веса = ' + str(bmi)+'\nУ Вас, ниже нормального веса.')
        elif 18.5 <= bmi < 25:
            bot.send_message(message.from_user.id, name+', индекс вашего веса = ' + str(bmi)+'\nУ Вас, нормальный вес.')
        elif 25 <= bmi < 30:
            bot.send_message(message.from_user.id, name+', индекс вашего веса = ' + str(bmi)+'\nУ Вас, избыточный вес.')
        elif 30 <= bmi < 35:
            bot.send_message(message.from_user.id, name+', индекс вашего веса = ' + str(bmi)+'\nУ Вас, ожирение I степени.')
        elif 35 <= bmi < 40:
            bot.send_message(message.from_user.id, name+', индекс вашего веса = ' + str(bmi)+'\nУ Вас, ожирение II степени.')
        elif 40 <= bmi:
            bot.send_message(message.from_user.id, name+', индекс вашего веса = ' + str(bmi)+'\nУ Вас, ожирение III степени.')

        bot.send_message(message.from_user.id, "\n_________________\nОтправьте 'Привет' чтобы начать заново")
    except Exception:
        bot.send_message(message.from_user.id, name + ', какой у Вас вес?\nНапример: 55')
        bot.register_next_step_handler(message, bwe)


bot.polling()
