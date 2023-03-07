import telebot

from telebot import types

bot = telebot.TeleBot('')

name = ''
age = 0
rost = 0
we = 0


@bot.message_handler(commands=['start', 'help'])
def start(message):
    name = message.from_user.first_name
    bot.send_message(message.from_user.id, name + ', какой у Вас рост?\nНапример: 160')
    bot.register_next_step_handler(message, brost)

    

def brost(message):
    global rost
    name = message.from_user.first_name
    rost = float(message.text) / 100
    bot.send_message(message.from_user.id, name + ', какой у Вас вес?')
    bot.register_next_step_handler(message, bwe)


def bwe(message):
    global we
    name = message.from_user.first_name
    we = float(message.text)
    bmi = float(we) / float(rost) ** 2
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
    bot.send_message(message.from_user.id, "\n_________________\nHачать заново /start")


bot.polling()

