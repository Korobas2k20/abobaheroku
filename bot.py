import telebot

bot = telebot.TeleBot('5187338543:AAHmrsONJOGURXBfu57x6tQRdXpcG46jWN8', parse_mode = None)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.TeleBot.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = telebot.TeleBot.KeyboardButton('Наши филиалы')
    item2 = telebot.TeleBot.KeyboardButton('Как оплатить?')
    item3 = telebot.TeleBot.KeyboardButton('Кто самый крутой?')
    item4 = telebot.TeleBot.KeyboardButton('Записаться (связь с администратором)')
    item5 = telebot.TeleBot.KeyboardButton('Стоимость')
    
    markup.add(item1, item2, item3, item4, item5)
    
    bot.send_message(message.chat.id, 'Здравствуйте, {0.first_name}'.format(message.from_user), reply_markup=markup)
    
#Получение сообщений через кнопки
@bot.message_handler(content_types= ['text'])
def bot_message(message):
    if message.chat.type == 'private' or 'public': # пишем в лс
        if message.text == 'Наши филиалы':
            bot.send_message(message.chat.id, 'У нас всего 5 филиалов по всему городу: \n\n Интернациональная, 10 \n Озерная 1 \n Салманова, 5 \n Омская, 12А \n Школа №32')
        elif message.text == 'Как оплатить?':
            bot.send_message(message.chat.id, 'Вы можете сделать это перед занятием или через сбербанк онлайн по номеру телефона 89527167444 (Михаил Геннадиевич Ш)')
        elif message.text == 'Кто самый крутой?':
            bot.send_message(message.chat.id, 'Андрей Стороженко')
        elif message.text == 'Записаться (связь с администратором)':
            bot.send_message(message.chat.id, 'Для связи с администратором👇\n \n@L00kyman \n@AdamGrella')
        elif message.text == 'Стоимость':
            bot.send_message(message.chat.id, 'Курс расчитан на один учебный год и включает в себя 4 модуля:\n\n🔹Компьютерная грамотность \n🔹3D моделирование\n🔹Программирование\n🔹IT проектирование \n\nАбонемент на месяц (4 занятия) - 4500 рублей. \nОдно занятие - 1125 рублей. \n\nДлительность одного занятия - 2 часа.\n\n Возраст - от 6 лет.')


bot.polling(none_stop=True) # безперерывная работа бота