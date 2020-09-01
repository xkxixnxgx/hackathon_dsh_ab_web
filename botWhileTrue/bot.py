import telebot
from telebot import types # pytelegrambotapi
from random import choice

import menu
import questions
import user
import mongo


token = '1293518313:AAET6K3HObbgrZT_gt2-EAVxqyqoMr2XfQg'

# bot = telebot.TeleBot(token, num_threads=8)
bot = telebot.AsyncTeleBot(token)

print("Bot has been started")

@bot.message_handler(commands=['start'])
def start_message(message):
    # Создание нового пользователя
    user.create(message.chat.id, message.chat.username)

    # выводим клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    markup.add(*menu.start)

    text = "".join([
        f"Здравствуйте, {message.from_user.first_name}!\n",
        # f"Вас приветствует - <b>{bot.get_me().first_name}</b>.\n\n",
        "Выберите необходимый пункт меню:\n",
    ])

    # приветствие после команды /start
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)


# Сервисы
@bot.message_handler(
    content_types=['text', 'document', 'photo'],
    func=lambda message: message.chat.type == 'private')
def services(message):
    if not user.check(message.chat.id): user.create(message.chat.id, message.chat.username)
    if message.text == "Заявки":
        bot.send_message(message.chat.id, "Загрузка данных...")
        data = mongo.get_data(message.chat.id)
        if not data: bot.send_message(message.chat.id, "Заявки не найдены.")
        for app in data:
            text = "".join([
                f"Тип продукта: {app['service']}!\n",
                f"Имя продукта: {app['proposal']}.\n",
                f"Статус: {app['status']}.",
            ])
            bot.send_message(message.chat.id, text)
    elif message.text == "Специалист":
        # bot.send_message(message.chat.id, "Данный раздел находится в разработке.\nПриносим свои извинения.")
        bot.send_message(message.chat.id, 'Запрос Отправлен.\nВ ближайшее время с вами свяжется специалист банка.')
        bot.send_message(chat_id=1184113473, text=f'Клиент @{message.chat.username} просит начать консультацию.')
    else:
        user_message = message.text
        user.set(message.chat.id, service=user_message)

        try:
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(*menu.services[user_message])
            bot.send_message(message.chat.id, choice(menu.service_messages), reply_markup=markup)
        except KeyError:
            bot.send_message(message.chat.id, 'Неверная команда')


# Оформление заявки
@bot.callback_query_handler(func=lambda call: call.data == 'submit')
def submit(call):
    user_info = user.get(call.message.chat.id)
    user.set(call.message.chat.id, reg_form=questions.start(user_info['service']))

    text = "".join([
        f"Тип продукта: {user_info['service']}!\n",
        f"Имя продукта: {user_info['proposal']}.\n\n",
        "Желаете продолжить?",
    ])

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Продолжить"))
    markup.add(types.KeyboardButton("Отмена"))
    bot.send_message(call.message.chat.id, text, reply_markup=markup)

    bot.register_next_step_handler(call.message, is_accept)


def is_accept(message):
    if message.text == "Продолжить":
        return ask_question(message)
        # bot.register_next_step_handler(message, ask_question)
    elif message.text == "Отмена":
        user.user_dict[message.chat.id]['reg_form'] = None
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        markup.add(*menu.start)
        bot.send_message(message.chat.id, "Заявка отменена.", reply_markup=markup)


def ask_question(message):
    try:
        question = next(user.user_dict[message.chat.id]['reg_form'])
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Пропустить"))
        markup.add(types.KeyboardButton("Отмена"))
        
        bot.send_message(message.chat.id, question[1], reply_markup=markup)
        bot.register_next_step_handler(message, get_answer, question)
    except StopIteration:
        bot.send_message(message.chat.id, "Оформление заявки...")
        
        # Запись в бд
        to_transfer = user.prapare(message.chat.id)
        mongo.write_data(to_transfer)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        markup.add(*menu.start)
        bot.send_message(message.chat.id, "Ваша заявка принята.\nСтатус заявки можно посмотреть в меню Заявки", reply_markup=markup)

    except KeyError:
        print(question)
        

def get_answer(message, question):
    if message.text == "Пропустить": return ask_question(message)
    elif message.text == "Отмена": return is_accept(message)
    else:
        user.user_dict[message.chat.id]['data'][question[0]] = message.text
        return ask_question(message)


# Назад
@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back(call):
    # proposal = call.data

    message = call.message
    # message.text = user.get(call.message.chat.id)['service'] # Текущий сервис
    message.text = user.user_dict[call.message.chat.id]['service'] # Текущий сервис
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(*menu.services[message.text])

    bot.edit_message_text(
        choice(menu.service_messages), 
        call.message.chat.id, 
        call.message.message_id, reply_markup=markup
    )


# Обработка предложений
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        try:
            proposal = call.data
            # user['proposal'] = menu.proposals[proposal]['name']
            user.set(call.message.chat.id, proposal=menu.proposals[proposal]['name'])
            

            markupupup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Оставить заявку", callback_data='submit')
            item2 = types.InlineKeyboardButton("Назад", callback_data='back')
            markupupup.add(item1, item2)

            #bot.send_message(call.message.chat.id, menu.proposals[proposal], reply_markup=markupupup)
            bot.edit_message_text(
                f"{menu.proposals[proposal]['message']}:\n{menu.proposals[proposal]['link']}", 
                call.message.chat.id, 
                call.message.message_id, reply_markup=markupupup
            )
        except KeyError:
            bot.send_message(call.message.chat.id, "В разработке")


# СТАРТ
if __name__ == '__main__':
    # bot.polling(none_stop=True, interval=0)
    bot.polling(timeout=100)