import telebot
from dodoBotDB import db, Users, CourierTest, OnboardingCheck, PizzamakerTest, ManagerTest, AdminTest
from telebot import types
import datetime

#testapi
#bot = telebot.TeleBot('6113223338:AAHpFLfKH913UZDI8tjNJdQjRpVmngAsnK4')
#real_api
bot = telebot.TeleBot('5893730597:AAEt1dhM0JIKnnMI8iIo_i32bEJgGkhlXU4')



@bot.message_handler(commands=['start'])
def welcome(message):
    if db.session.query(Users.username).filter_by(username=message.from_user.username).first() is None:
        db.session.add(Users(username=message.from_user.username, first_name=message.from_user.first_name,
                            last_name=message.from_user.last_name, chat_id=message.chat.id))
        db.session.commit()
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton('Конечно!', callback_data="firstmsg")
    markup.add(btn)
    bot.send_message(message.chat.id,'Привет! Рады тебя видеть в рядах команды Додо😊🦤 Хочешь узнать нас получше'
                                     '?'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.message:
        if call.data == "firstmsg":
            file = open('static/img/dodoshka.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn=types.InlineKeyboardButton('Начать знакомство🤝',callback_data="mainmenu")
            markup.add(btn)
            bot.send_photo(call.message.chat.id, file,
                           caption='Людям нравится работать, когда они чувствуют свою ценность. В большой компании '
                                   'человек может теряться, чувствовать себя менее значимым.Мы в Додо уверены: чем '
                                   'больше компания, тем больше внимания должно быть к тем, кто с ней работает.',
                           reply_markup=markup)

        if call.data=="mainmenu":
            file = open('static/img/mainmenu.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Обучение должностям🎓', callback_data="training")
            btn1 = types.InlineKeyboardButton('Наши принципы🦤', callback_data='about')
            btn2 = types.InlineKeyboardButton('Топ меню🔝', callback_data='pizzamenu')
            btn3 = types.InlineKeyboardButton('Знакомство с рабочим местом🏢', callback_data='workplace')
            btn4 = types.InlineKeyboardButton('Познакомиться с командой👥', callback_data='team')
            markup.add(btn, btn1, btn2, btn3, btn4)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Выбери, о чем ты хочешь узнать❓'), reply_markup=markup)


        if call.data == "team":
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Вперед➡', callback_data='stas')
            btn1 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1)
            file = open('static/img/team.png', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='В каждой пиццерии сети работают те, кто хочет приходить '
                                                                       'к нам с удовольствием каждый день. Сейчас мы познакомим '
                                                                       'тебя с теми, с кем тебе придется работать бок о бок, и к кому '
                                                                       'ты сможешь обратиться за советом🤗'),
                                   reply_markup=markup)

        if call.data == "stas":
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='team')
            btn1 = types.InlineKeyboardButton('Вперед➡', callback_data='alexandra')
            btn2 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1, btn2)
            file = open('static/img/stas.png', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Это Стас - пиццамейкер в твоей пиццерии. Любит слушать музыку🎧, '
                                                                       'играть в футбол⚽ и знакомиться с новыми людьми🗣️. Не стесняйся '
                                                                       'и познакомься с ним, как встретишь, он будет рад🤩!'),
                                   reply_markup=markup)

        if call.data == "alexandra":
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='stas')
            btn1 = types.InlineKeyboardButton('Вперед➡', callback_data='nikita')
            btn2 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1, btn2)
            file = open('static/img/alexandra.png', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Это Александра - твой менеджер. Любит смотреть сериалы📺 и '
                                                                       'заниматься фитнесом🧘‍♀. Она - человек с характером, но мы уверены, '
                                                                       'вы с ней поладите😉!'),
                                   reply_markup=markup)

        if call.data == "nikita":
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='alexandra')
            btn1 = types.InlineKeyboardButton('Вперед➡', callback_data='others')
            btn2 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1, btn2)
            file = open('static/img/nikita.png', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Это Никита - наш курьер. Любит ходить на рыбалку🎣 и '
                                                                       'спать🛌. А ещё он обожает сыр🧀'
                                                                       'Отвечает не очень часто, но он всё равно станет тебе '
                                                                       'хорошим другом☺'),
                                   reply_markup=markup)

        if call.data == "others":
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='nikita')
            btn1 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1)
            file = open('static/img/others.png', 'rb')
            enter = "\n"
            people = db.session.query(Users).all()
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption=f'А здесь ты можешь увидеть ссылки на новичков - да-да, '
                                                                       'таких же, как ты (ты там тоже есть)😉 Списывайтесь, общайтесь, будьте командой!💪\n'
                                                                       +f'{f"".join(f"@{row.username}{enter}"for row in people)}'),
                                   reply_markup=markup)




        if call.data == "pizzamenu":
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Вперед➡', callback_data='richtaste')
            btn1 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1)
            file = open('static/img/diablo.png', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Пицца Диабло🌶️🌶️🌶️, подойдёт для любителей остренького\n '
                                                               'Острый халапеньо в сочетании с острой чоризо, барбекю '
                                                               'соусом, беконом и остальными ингредиентами даёт сочный '
                                                               'вкус и остроту, это незабываемый вкус'), reply_markup=markup)

        if call.data == "richtaste":
            file = open('static/img/der.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='pizzamenu')
            btn1 = types.InlineKeyboardButton('Вперед➡', callback_data='meat')
            btn2 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1, btn2)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                   caption='Пицца Деревенская с бужениной😋😋😋 прекрасно подойдет тем кто любит много есть.'
                                       '\n запеченная буженина из свинины, моцарелла, картофель из печи, маринованные огурчики, '
                                       'фирменные томатный соус и соус ранч дают своей незабываемый вкус и никто не останется равнодушным'),
                                    reply_markup=markup)

        if call.data == "meat":
            file = open('static/img/mix.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='richtaste')
            btn1 = types.InlineKeyboardButton('Вперед➡', callback_data='cheese')
            btn2 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1, btn2)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Пиццу Мясной Микс🥩🥩🥩 по настоящему оценят любители большого колличества '
                                       'мясной начинки в пицце\nЗапеченная буженина из свинины, острая чоризо, пикантная '
                                       'пепперони, бекон в совокупности с фирменным томатным соусом дают волшебный вкус'),
                                   reply_markup=markup)

        if call.data == "cheese":
            file = open('static/img/sir.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='meat')
            btn1 = types.InlineKeyboardButton('Вперед➡', callback_data='mix')
            btn2 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1, btn2)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Пицца Сырный цыпленок🧀🐥 подойдет для любителей сыра\n'
                                                                       'В её составе не много '
                                       'ингредиентов, но их сочетание прекрасно\nЦыпленок, моцарелла, сыры чеддер и '
                                       'пармезан, сырный соус, томаты, фирменный соус альфредо дают прекрасный вкус'),
                                   reply_markup=markup)

        if call.data == "mix":
            file = open('static/img/kons.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='cheese')
            btn1 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='И закрывает наш топ Пицца-конструктор🍕🔧 \n'
                                                                       'В основе увеличенная порция моцареллы и '
                                       'фирменный томатный соус, а другие ингредиенты можно выбрать на свой вкус.\n'
                                       'Это прекрасная возможность собрать свой микс и наслаждаться вкусом'),
                                   reply_markup=markup)







        if call.data == "workplace":
            file = open('static/img/kyhna.jpg', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Вперед➡', callback_data='cashout')
            btn1 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='На кухне🧑‍🍳 происходит готовка пицц,закусок и десертов.'
                                                                       '\n Из сотрудников на кухне находятся пиццамейкеры и менеджер'),
                                   reply_markup=markup)

        if call.data == "cashout":
            file = open('static/img/kassa.jpg', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='workplace')
            btn1 = types.InlineKeyboardButton('Вперед➡', callback_data='courierzone')
            btn2 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1, btn2)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='На кассе💸 находится обычно менеджер и на ней '
                                                                       'же выдаются заказы посетителям'),
                                   reply_markup=markup)

        if call.data == "courierzone":
            file = open('static/img/zona.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='cashout')
            btn1 = types.InlineKeyboardButton('Вперед➡', callback_data='office')
            btn2 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1, btn2)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='В курьерской зоне🚴🍕 собираются заказы на доставку'
                                                                       'там в основном находятся только курьеры, но к ним'
                                                                       'на проверку чистоты может зайти менеджер или управляющий'),
                                   reply_markup=markup)

        if call.data == "office":
            file = open('static/img/ofis.jpg', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='cashout')
            btn1 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='В офисе🖥️ происходит управление пиццерии это как '
                                                                       'мозг у человека, а остальное - это тело, которому '
                                                                       'идут команды от мозга.\nВ основном там находятся '
                                                                       'управляющий и менеджер. '),
                                   reply_markup=markup)



        if call.data == "about":
            file = open('static/img/dodoshka.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Вперед➡', callback_data='ingredients')
            btn1 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn,btn1)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Обычно люди приходят в Додо Пиццу, чтобы просто '
                                                                       'поесть. Наши промоутеры раздают листовки про кусочек '
                                                                       'пиццы. '
                                                                       'Мы делаем это как первый шаг, чтобы познакомиться.\nНо '
                                                                       'для нас Додо — не только пицца. Это и пицца тоже, '
                                                                       'но в первую очередь это большое дело, которое '
                                                                       'вдохновляет нас, заставляет каждое утро просыпаться '
                                                                       'и с интересом продолжать работу.\nВ чём же наш '
                                                                       'интерес? Сейчас расскажем.'),
                                   reply_markup=markup)

        if call.data == "ingredients":
            file = open('static/img/piza.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='about')
            btn1 = types.InlineKeyboardButton('Вперед➡', callback_data='taste')
            btn2 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1, btn2)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Почему мы так хотим познакомиться? Потому что '
                                                                       'дальше пицца делает всё сама. Люди видят, '
                                                                       'что она вкусная, и возвращаются снова. Нам главное '
                                                                       'первый раз это показать.Вообще пицца — очень '
                                                                       'простая штука, её сложно испортить. Достаточно '
                                                                       'хороших ингредиентов и правильного теста. Это '
                                                                       'конструктор, если детали качественные, то и '
                                                                       'результат будет в порядке. Вот они, наши детали⬆.'),
                                   reply_markup=markup)

        if call.data == "taste":
            file = open('static/img/graf.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Назад⬅', callback_data='ingredients')
            btn1 = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='mainmenu')
            markup.add(btn, btn1)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Кто угодно может сделать вкусную пиццу. А '
                                                                       'шеф-повар итальянского ресторана сделает и вовсе '
                                                                       'шедевр. Он молодец. Но представьте, что вам нужно '
                                                                       'сделать вкусную пиццу в сотнях пиццерий, за сотни '
                                                                       'километров друг от друга. \n\n Пицца должна быть '
                                                                       'вкусной и везде одинаковой. Пиццерии должны быть '
                                                                       'одинаково уютными, кассиры неизменно приветливыми, '
                                                                       'а курьеры — расторопными.\n\nИ это как раз сложно. '
                                                                       'Но мы умеем! И вас научим😉'),
                                   reply_markup=markup)


        if call.data == 'training':
            file = open('static/img/training.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Курьер🏎️💨', callback_data='courier')
            btn1 = types.InlineKeyboardButton('Пиццамейкер🍕😋', callback_data='pizzamaker')
            btn2 = types.InlineKeyboardButton('Менеджер📋', callback_data='manager')
            btn3 = types.InlineKeyboardButton('Управляющий👑', callback_data='administrator')
            btn4 = types.InlineKeyboardButton('Вернуться на главную', callback_data='mainmenu')
            markup.add(btn, btn1, btn2, btn3, btn4)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Выбери свою должность✅'),
                                   reply_markup=markup)

        if call.data == "courier":
            file = open('static/img/kyrer_logo.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Пройти тест', callback_data='couriertest')
            btn1 = types.InlineKeyboardButton('Вернуться на главную', callback_data='mainmenu')
            markup.add(btn, btn1)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Курьер забирает и привозит пиццу клиенту на '
                                                                       'своем личном авто.\nВ обязанностях курьера '
                                                                       'доставить пиццу вовремя и тепленькой, а также '
                                                                       'принимать оплату.\nВнешний вид курьера: в '
                                                                       'обязательном порядке должна быть брендированная '
                                                                       'верхняя одежда, в тёплое время футболка или '
                                                                       'жилетка с логотипом, а зимой тёплая куртка.'),
                                   reply_markup=markup)

        if call.data == "couriertest":
            file = open('static/img/test.png', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Сейчас тебе предстоит пройти тест на должность курьера. '
                                                                       'Тебе зададут 3 вопроса с двумя вариантами ответа. Чтобы '
                                                                       'ответить на тест, просто отправь боту сообщение с последовательностью '
                                                                       'цифр 1 и 2 через пробел: первая цифра - ответ на первый вопрос, вторая - на второй и так далее '
                                                                       '(пример: 1 2 3). '
                                                                       'Просто, не так ли?😉 Ну что, ты готов? Введи любой текст для начала тестирования!'))
            bot.register_next_step_handler(call.message, couriertest)

        if call.data == "pizzamaker":
            file = open('static/img/maker_logo.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Пройти тест', callback_data='pizzamakertest')
            btn1 = types.InlineKeyboardButton('Вернуться на главную', callback_data='mainmenu')
            markup.add(btn, btn1)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Пиццамейкеры - это короли кхни, от пиццамейкера '
                                                                       'зависит, получит ли гость удовольствие.\nРасскажем '
                                                                       'немного о самом процессе готовки.\nВообще пицца — '
                                                                       'очень простая штука, её сложно испортить. Достаточно '
                                                                       'хороших ингредиентов и правильного теста. Это '
                                                                       'конструктор, если детали качественные, то и '
                                                                       'результат будет в порядке.\nТакже в обязанности '
                                                                       'пиццамейкера входит поддержание чистоты на рабочем '
                                                                       'месте, заготовка ингредиентов и принятие поставок продуктов.'),
                                   reply_markup=markup)

        if call.data == "pizzamakertest":
            file = open('static/img/test.png', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Сейчас тебе предстоит пройти тест на должность пиццамейкера. '
                                                                       'Тебе зададут 3 вопроса с двумя вариантами ответа. Чтобы '
                                                                       'ответить на тест, просто отправь боту сообщение с последовательностью '
                                                                       'цифр 1 и 2 через пробел: первая цифра - ответ на первый вопрос, вторая - на второй и так далее '
                                                                       '(пример: 1 2 3). '
                                                                       'Просто, не так ли?😉 Ну что, ты готов? Введи любой текст для начала тестирования!'))
            bot.register_next_step_handler(call.message, pizzamakertest)

        if call.data == "manager":
            file = open('static/img/manager_logo.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Пройти тест', callback_data='managertest')
            btn1 = types.InlineKeyboardButton('Вернуться на главную', callback_data='mainmenu')
            markup.add(btn, btn1)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Менеджер - это связующее звену между всей командой. '
                                                                       '\nМенеджер помогает все персоналу, следит за '
                                                                       'выполнением обязанностей, помогает пиццамейкерам '
                                                                       'в готовке, открывает и закрывает смены сотрудникам\n'
                                                                       'В основном задача менеджера следить за порядком и '
                                                                       'работать с клиентами\nРабота с клиентами является '
                                                                       'главной задачей менеджера, работа с клиентами '
                                                                       'может проявляться от консультации до решения '
                                                                       'каких-то конфликтов.'),
                                   reply_markup=markup)

        if call.data == "managertest":
            file = open('static/img/test.png', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Сейчас тебе предстоит пройти тест на должность менеджера. '
                                                                       'Тебе зададут 3 вопроса с двумя вариантами ответа. Чтобы '
                                                                       'ответить на тест, просто отправь боту сообщение с последовательностью '
                                                                       'цифр 1 и 2 через пробел: первая цифра - ответ на первый вопрос, вторая - на второй и так далее '
                                                                       '(пример: 1 2 3). '
                                                                       'Просто, не так ли?😉 Ну что, ты готов? Введи любой текст для начала тестирования!'))
            bot.register_next_step_handler(call.message, managertest)

        if call.data == "administrator":
            file = open('static/img/yprav_logo.png', 'rb')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton('Пройти тест', callback_data='admintest')
            btn1 = types.InlineKeyboardButton('Вернуться на главную', callback_data='mainmenu')
            markup.add(btn, btn1)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Управляющий - это организатор.\nУправляющий '
                                                                       'организует работу всей пиццерии от и до.\n '
                                                                       'На плечах управляющего лежит развитие команды '
                                                                       ',что очень важно.\nКонтроль показателей всей '
                                                                       'пиццерии является основной работой управляющего, '
                                                                       'он должен ставить приоритеты по показателям кухне, '
                                                                       'например время готовки пиццы и время доставки для '
                                                                       'курьеров.\nТакже управляющий общается с '
                                                                       'поставщиками, проводит инвентаризацию и собрания '
                                                                       'пиццерии, где обсуждаются нужды сотрудников, '
                                                                       'ведь Dodo пицца - это семья ❤.'),
                                   reply_markup=markup)

        if call.data == "admintest":
            file = open('static/img/test.png', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   media=types.InputMediaPhoto(media=file,
                                                               caption='Сейчас тебе предстоит пройти тест на должность управляющего. '
                                                                       'Тебе зададут 3 вопроса с двумя вариантами ответа. Чтобы '
                                                                       'ответить на тест, просто отправь боту сообщение с последовательностью '
                                                                       'цифр 1 и 2 через пробел: первая цифра - ответ на первый вопрос, вторая - на второй и так далее '
                                                                       '(пример: 1 2 3). '
                                                                       'Просто, не так ли?😉 Ну что, ты готов? Введи любой текст для начала тестирования!'))
            bot.register_next_step_handler(call.message, admintest)


def couriertest(message):
    questions = db.session.query(CourierTest).all()
    for elem in questions:
        bot.send_message(message.chat.id, elem.question)
    bot.send_message(message.chat.id, 'Как будешь готов ответить - введи цифры ответов на все вопросы в одну строку через пробел😀')
    bot.register_next_step_handler(message, couriertest_result)

def couriertest_result(message):
    right_answers = db.session.query(CourierTest).all()
    answers_user = message.text.split()
    total = 0
    i = 0
    for elem in right_answers:
        if elem.answer == answers_user[i]:
            total += 1
        i += 1
    db.session.add(OnboardingCheck(username=message.from_user.username,onboarding_type='Курьер',result=f'{total}/{len(right_answers)}',
                                   time=datetime.datetime.now()))
    db.session.commit()
    file = open('static/img/test.png', 'rb')
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton('Вернуться на главную', callback_data='mainmenu')
    markup.add(btn)
    bot.send_photo(message.chat.id, file,
                   caption=f'Твой результат: {total}/{len(right_answers)}✅',
                   reply_markup=markup)

def pizzamakertest(message):
    questions = db.session.query(PizzamakerTest).all()
    for elem in questions:
        bot.send_message(message.chat.id, elem.question)
    bot.send_message(message.chat.id, 'Как будешь готов ответить - введи цифры ответов на все вопросы в одну строку через пробел😀')
    bot.register_next_step_handler(message, pizzamakertest_result)

def pizzamakertest_result(message):
    right_answers = db.session.query(PizzamakerTest).all()
    answers_user = message.text.split()
    total = 0
    i = 0
    for elem in right_answers:
        if elem.answer == answers_user[i]:
            total += 1
        i += 1
    db.session.add(OnboardingCheck(username=message.from_user.username,onboarding_type='Пиццамейкер',result=f'{total}/{len(right_answers)}',
                                   time=datetime.datetime.now()))
    db.session.commit()
    file = open('static/img/test.png', 'rb')
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton('Вернуться на главную', callback_data='mainmenu')
    markup.add(btn)
    bot.send_photo(message.chat.id, file,
                   caption=f'Твой результат: {total}/{len(right_answers)}✅',
                   reply_markup=markup)

def managertest(message):
    questions = db.session.query(ManagerTest).all()
    for elem in questions:
        bot.send_message(message.chat.id, elem.question)
    bot.send_message(message.chat.id, 'Как будешь готов ответить - введи цифры ответов на все вопросы в одну строку через пробел😀')
    bot.register_next_step_handler(message, managertest_result)

def managertest_result(message):
    right_answers = db.session.query(ManagerTest).all()
    answers_user = message.text.split()
    total = 0
    i = 0
    for elem in right_answers:
        if elem.answer == answers_user[i]:
            total += 1
        i += 1
    db.session.add(OnboardingCheck(username=message.from_user.username,onboarding_type='Менеджер',result=f'{total}/{len(right_answers)}',
                                   time=datetime.datetime.now()))
    db.session.commit()
    file = open('static/img/test.png', 'rb')
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton('Вернуться на главную', callback_data='mainmenu')
    markup.add(btn)
    bot.send_photo(message.chat.id, file,
                   caption=f'Твой результат: {total}/{len(right_answers)}✅',
                   reply_markup=markup)

def admintest(message):
    questions = db.session.query(AdminTest).all()
    for elem in questions:
        bot.send_message(message.chat.id, elem.question)
    bot.send_message(message.chat.id, 'Как будешь готов ответить - введи цифры ответов на все вопросы в одну строку через пробел😀')
    bot.register_next_step_handler(message, admintest_result)

def admintest_result(message):
    right_answers = db.session.query(AdminTest).all()
    answers_user = message.text.split()
    total = 0
    i = 0
    for elem in right_answers:
        if elem.answer == answers_user[i]:
            total += 1
        i += 1
    db.session.add(OnboardingCheck(username=message.from_user.username,onboarding_type='Управляющий',result=f'{total}/{len(right_answers)}',
                                   time=datetime.datetime.now()))
    db.session.commit()
    file = open('static/img/test.png', 'rb')
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton('Вернуться на главную', callback_data='mainmenu')
    markup.add(btn)
    bot.send_photo(message.chat.id, file,
                   caption=f'Твой результат: {total}/{len(right_answers)}✅',
                   reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)

