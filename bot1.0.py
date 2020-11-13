import telebot
from telebot import types
import config
request_location=True
from string import Template
import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot("1387989780:AAElHMeKEgKUxAu9pvZtEXFWZnlglpX5gZE")

user_dict = {}


#(bot.get_chat('@https://t.me/GGYcc44').id)


@bot.message_handler(commands=['social_networks'])
def social_networks(message):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='INSTAGRAMM', url='https://www.instagram.com/_7_eugene_8_/')
        btn_my_site1 = types.InlineKeyboardButton(text='VK', url='https://vk.com/id444964380')
        markup.add(btn_my_site,btn_my_site1,)
        bot.send_message(message.chat.id, "Нажми на кнопку и перейди на мою социальную сеть.", reply_markup=markup)
        bot.send_message(message.chat.id, '==>> /help <<== нажми')

r = requests.get('https://sinoptik.ua/погода-санкт-петербург')
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text

@bot.message_handler(commands=['wes'])
def wes(message):
	bot.send_message(message.chat.id, "Привет, погода на сегодня:\n" +
        t_min + ', ' + t_max + '\n' + text)



class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'driverSeria',
                'driverNumber', 'driverDate', 'car',
                'carModel', 'carColor', 'carNumber', 'carDate']
        for key in keys:
            self.key = None


@bot.message_handler(commands=["reg"])
def user_reg(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Москва')
    itembtn2 = types.KeyboardButton('СПб')
    itembtn3 = types.KeyboardButton('ЕКб')
    itembtn4 = types.KeyboardButton('Новосибирск')
    itembtn5 = types.KeyboardButton('Краснодар')
    itembtn6 = types.KeyboardButton('Мурманск')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

    msg = bot.send_message(message.chat.id, 'Ваш город?', reply_markup=markup)
    bot.register_next_step_handler(msg, process_city_step)


def process_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Фамилия Имя Отчество', reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'Ваш номер телефона')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        bot.reply_to(message, 'Что то пошло не так....!')


def process_phone_step(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, 'Серия водительского удостоверения')
        bot.register_next_step_handler(msg, process_driverSeria_step)

    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step)


def process_driverSeria_step(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverSeria = message.text

        msg = bot.send_message(chat_id, 'Номер водительского удостоверения')
        bot.register_next_step_handler(msg, process_driverNumber_step)

    except Exception as e:
        bot.reply_to(message, 'Вы ввели что то другое!!')


def process_driverNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverNumber = message.text

        msg = bot.send_message(chat_id, 'Дата выдачи водительского удостоверения\nВ формате: День.Месяц.Год')
        bot.register_next_step_handler(msg, process_driverDate_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_driverDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverDate = message.text

        msg = bot.send_message(chat_id, 'Марка автомобиля')
        bot.register_next_step_handler(msg, process_car_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_car_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.car = message.text

        msg = bot.send_message(chat_id, 'Модель автомобиля')
        bot.register_next_step_handler(msg, process_carModel_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_carModel_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carModel = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Бежевый')
        itembtn2 = types.KeyboardButton('Белый')
        itembtn3 = types.KeyboardButton('Голубой')
        itembtn4 = types.KeyboardButton('Желтый')
        itembtn5 = types.KeyboardButton('Зеленый')
        itembtn6 = types.KeyboardButton('Коричневый')
        itembtn7 = types.KeyboardButton('Красный')
        itembtn8 = types.KeyboardButton('Оранжевый')
        itembtn9 = types.KeyboardButton('Розовый')
        itembtn10 = types.KeyboardButton('Серый')
        itembtn11 = types.KeyboardButton('Синий')
        itembtn12 = types.KeyboardButton('Фиолетовый')
        itembtn13 = types.KeyboardButton('Черный')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10,
                   itembtn11, itembtn12, itembtn13)

        msg = bot.send_message(chat_id, 'Цвет автомобиля', reply_markup=markup)
        bot.register_next_step_handler(msg, process_carColor_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_carColor_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carColor = message.text

        msg = bot.send_message(chat_id, 'Гос. номер автомобиля')
        bot.register_next_step_handler(msg, process_carNumber_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_carNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carNumber = message.text

        msg = bot.send_message(chat_id, 'Год выпуска')
        bot.register_next_step_handler(msg, process_carDate_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def process_carDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carDate = message.text

        # ваша заявка "Имя пользователя"
        bot.send_message(chat_id, getRegData(user, 'Ваша заявка', message.from_user.first_name), parse_mode="Markdown")

        bot.send_message(config.chat_id, getRegData(user, 'Заявка от бота', bot.get_me().username),parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template(
        '$title *$name* \n Город: *$userCity* \n ФИО: *$fullname* \n Телефон: *$phone* \n Серия водительского удостоверения: *$driverSeria* \n Номер водительского удостоверения: *$driverNumber* \n Дата выдачи водительского удостоверения: *$driverDate* \n Марка автомобиля: *$car* \n Модель автомобиля: *$carModel* \n Цвет автомобиля: *$carColor* \n Гос. номер автомобиля: *$carNumber* \n Год выпуска: *$carDate*')

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        'driverSeria': user.driverSeria,
        'driverNumber': user.driverNumber,
        'driverDate': user.driverDate,
        'car': user.car,
        'carModel': user.carModel,
        'carColor': user.carColor,
        'carNumber': user.carNumber,
        'carDate': user.carDate,
    })


# произвольный текст



# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!

bot.register_next_step_handler






@bot.message_handler(commands = ['switch'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query="Telegram")
    markup.add(switch_button)
    bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)
    bot.send_message(message.chat.id, "/help")

user_num1 = ''
user_num2 = ''
user_proc = ''
user_result = None

# если /start, /help
@bot.message_handler(commands=['cul'])
def cul(message):
    # убрать клавиатуру Telegram полностью
    markup = types.ReplyKeyboardRemove(selective=False)

    msg = bot.send_message(message.chat.id, "Привет " + message.from_user.first_name + ", я бот-калькулятор\nВведите число", reply_markup=markup)
    bot.register_next_step_handler(msg, process_num1_step)


def process_num1_step(message, user_result = None):
    try:
       global user_num1


       if user_result == None:
          user_num1 = int(message.text)
       else:
          # если был передан результат ранее
          # пишем в первое число, не спрашивая
          user_num1 = str(user_result)

       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
       itembtn1 = types.KeyboardButton('+')
       itembtn2 = types.KeyboardButton('-')
       itembtn3 = types.KeyboardButton('*')
       itembtn4 = types.KeyboardButton('/')
       markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

       msg = bot.send_message(message.chat.id, "Выберите операцию", reply_markup=markup)
       bot.register_next_step_handler(msg, process_proc_step)
    except Exception as e:
       bot.reply_to(message, 'Это не число или что то пошло не так...')

# выберите операцию +, -, *, /
def process_proc_step(message):
    try:
       global user_proc

       # запоминаем операцию
       user_proc = message.text
       # убрать клавиатуру Telegram полностью
       markup = types.ReplyKeyboardRemove(selective=False)

       msg = bot.send_message(message.chat.id, "Введите еще число", reply_markup=markup)
       bot.register_next_step_handler(msg, process_num2_step)
    except Exception as e:
       bot.reply_to(message, 'Вы ввели что то другое или что то пошло не так...')


def process_num2_step(message):
    try:
       global user_num2


       user_num2 = int(message.text)

       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
       itembtn1 = types.KeyboardButton('Результат')
       itembtn2 = types.KeyboardButton('Продолжить вычисление')
       markup.add(itembtn1, itembtn2)

       msg = bot.send_message(message.chat.id, "Показать результат или продолжить операцию?", reply_markup=markup)
       bot.register_next_step_handler(msg, process_alternative_step)
    except Exception as e:
       bot.reply_to(message, 'Это не число или что то пошло не так...')


def process_alternative_step(message):
    try:

       calc()


       markup = types.ReplyKeyboardRemove(selective=False)

       if message.text.lower() == 'результат':
          bot.send_message(message.chat.id, calcResultPrint(), reply_markup=markup)
       elif message.text.lower() == 'продолжить вычисление':
          process_num1_step(message, user_result )

    except Exception as e:
       bot.reply_to(message, 'Что то пошло не так...')


def calcResultPrint():
    global user_num1, user_num2, user_proc, user_result
    return "Результат: " + str(user_num1) + ' ' + user_proc + ' ' + str(user_num2) + ' = ' + str( user_result )


def calc():
    global user_num1, user_num2, user_proc, user_result

    user_result = eval(str(user_num1) + user_proc + str(user_num2))

    return user_result


bot.enable_save_next_step_handlers(delay=2)


bot.load_next_step_handlers()



name = ''
surname = ''
age = 0


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('1.Калькулятрор')
    itembtn2 = types.KeyboardButton('2.Анкета')
    itembtn3 = types.KeyboardButton('3.Контакты,геопозиция')
    itembtn4 = types.KeyboardButton('4.Начало')
    itembtn5 = types.KeyboardButton('5.Социальные сети')
    itembtn6 = types.KeyboardButton('6.Поделиться ботом')
    itembtn7 = types.KeyboardButton('7.Погода')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)


    message = bot.send_message(message.chat.id,  "1.Калькулятор - поможет с вычислением любых чисел....  " +
                                      " 2. В 'Анкета' ты можешь пройти небольшой опрос от бота .... " +
                                      " 3. С помощью третий кнопки бот узнает ваш номер телефона и вашу геолокацию... " +
                                      " 4. Четвертая кнопка переносит вас в самое начало  .... " +
                                      " 5. Пятая кнопка это ссылка на мои социальные сети  ...." +
                                      " 6. С помощью шестой кнопки вы можите поделиться этим ботом в телеграмм", reply_markup=markup)
def process_select_step(message):
    try:
        if (message.text == '1.Калькулятрор'):
            cul(message)
        elif (message.text == '6.Поделиться ботом'):
            switch(message)
        elif (message.text == '2.Анкета'):
           user_reg(message)
        elif (message.text == '3.Контакты,геопозиция'):
            geophone (message)
        elif (message.text == '4.Начало'):
            start(message)
        elif (message.text == '5.Социальные сети'):
            social_networks(message)
        elif (message.text == '7.Погода'):
            wes(message)
        else:
            bot.help(message)
    except Exception as e:
        bot.reply_to(message, 'Что то пошло не так...')





@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Hi', '/help', 'Пока')
    bot.send_message(message.chat.id,"Привет! " + message.from_user.first_name + ", Тебе чем то помочь? Нажми '/help', и узнай,что я могу!", reply_markup=keyboard)


@bot.message_handler(commands=["geophone"])
def geophone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!", reply_markup=keyboard)






@bot.message_handler(func=lambda m: True)
def message(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Привет создатель бота!')
    elif message.text == 'hi':
        bot.send_message(message.chat.id, 'Hi again!The bot creator!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'До свидания! Хорошего дня!)')
    elif message.text == 'Hi':
        bot.send_message(message.chat.id, 'Hi again! , ' + message.from_user.first_name + '! Нажми /help  и узнай ,что я могу!')
    elif message.text == 'привет':
        bot.send_message(message.chat.id, 'ПРИВЕТ! , ' + message.from_user.first_name)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn1 = types.KeyboardButton('Меню')
        markup.add(itembtn1)
        msg = bot.send_message(message.chat.id, "Нажмите кнопку ,чтобы перейти в меню!", reply_markup=markup)
        bot.register_next_step_handler(msg, process_select_step1)


def process_select_step1(message):
    try:
        if (message.text == 'Меню'):
            help(message)
        else:
            bot.help(message)
    except Exception as e:
        bot.reply_to(message, 'Что то пошло не так...')




if __name__ == '__main__':
    bot.polling(none_stop=True)
