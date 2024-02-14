import telebot
from telebot import types

bot = telebot.TeleBot('5988070379:AAGtWxqUromr6_QHOtSNa2WG1p9G4nfoICY')






@bot.message_handler(commands=['start', 'help', 'nexting', 'hi', 'bye','ser','solve', 'haveaniceday', 'youhaveerror', 'letsgo', 'error', 'howareyou', 'historiINUKRAIN', 'ukrainwrite', 'math', 'geometria', 'literaturaUA', 'vsesvitnayhistori', 'fizika', 'osnovZD', 'himiay', 'geografia', 'oruzh'])
def reply(message):
    if message.text == '/start':
        bot.reply_to(message, 'i have this is command(/next,/help,/hi,/bye,/solve,/ser,/haveaniceday,/youhaveerror,/letsgo,/error,/howareyou,/math,/ukrainwrite,/historiINUKRAIN,/geometria,/literaturaUA,/vsesvitnayhistori,/fizika,/osnovZD,/himiay,/geografia,/oruzh)')
    if message.text == '/hi':
        bot.reply_to(message, 'hi,what do you want leather dont bother me')
    if message.text == '/nexting':
        bot.reply_to(message, 'next i have(/math,/ukrainwrite,/historiINUKRAIN,/geometria,/literaturaUA,/vsesvitnayhistori,/fizika,/osnovZD,/himiay,/geografia,/oruzh)')
    if message.text == '/bye':
        bot.reply_to(message, 'goodbye user')
    if message.text == '/help':
        bot.reply_to(message, 'This is help command')
    if message.text == '/solve':
        bot.reply_to(message, 'pleas write you name')
    if message.text == '/haveaniceday':
        bot.reply_to(message, 'you too')
    if message.text == '/youhaveerror':
        bot.reply_to(message, 'no, i dont have error')
    if message.text == '/error':
        bot.reply_to(message, 'errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror')
    if message.text == '/howareyou':
        bot.reply_to(message, 'normal')
    if message.text == '/letsgo':
        bot.reply_to(message, 'ok')
    if message.text == '/math':
        bot.reply_to(message, 'https://pidruchnyk.com.ua/764-algebra-7-merzlyak-2015.html')
    if message.text == '/ukrainwrite':
        bot.reply_to(message, 'https://pidruchnyk.com.ua/761-ukrmova-7-klas-glazova-2015.html')
    if message.text == '/historiINUKRAIN':
        bot.reply_to(message, 'https://pidruchnyk.com.ua/1496-istoriya-ukrayiny-7-klas-schupak.html')
    if message.text == '/geometria':
        bot.reply_to(message, 'https://pidruchnyk.com.ua/698-geometriya-merzlyak-7klas-2015.html')
    if message.text == '/literaturaUA':
        bot.reply_to(message, 'https://shkola.in.ua/2091-ukrainska-literatura-7-klas-avramenko-2015.html')
    if message.text == '/vsesvitnayhistori':
        bot.reply_to(message, 'https://pidruchnyk.com.ua/1495-vsesvitnya-istoriya-7-klas-schupak-2020.html')
    if message.text == '/fizika':
        bot.reply_to(message, 'https://pidruchnyk.com.ua/1453-fzika-baryahtar-7-klas.html')
    if message.text == '/osnovZD':
        bot.reply_to(message, 'https://pidruchnyk.com.ua/744-osnovi-zdorovya-beh-voroncova-ponomarenko-strashko-7-klas.html')
    if message.text == '/himiay':
        bot.reply_to(message, 'https://pidruchnyk.com.ua/739-popel-himiya-7-klas-2015.html')
    if message.text == '/geografia':
        bot.reply_to(message, 'https://pidruchnyk.com.ua/700-geografiya-7-boyko-2015.html')
    keyboard = types.InlineKeyboardMarkup()
    if message.text == '/ser':
       btn111 = types.InlineKeyboardButton('1Hu tao', url='https://genshin-info.ru/wiki/personazhi/hu-tao/')
       btn122 = types.InlineKeyboardButton('2thin stu', url='https://genshin-info.ru/wiki/personazhi/xingqiu/')
       btn133 = types.InlineKeyboardButton('3Ayaka', url='https://genshin-info.ru/wiki/personazhi/ayaka/')
       btn144 = types.InlineKeyboardButton('4kadzuha', url='https://genshin-info.ru/wiki/personazhi/kadzukha/')
       btn155 = types.InlineKeyboardButton('5Noelle', url='https://genshin-info.ru/wiki/personazhi/noelle/')
       btn166 = types.InlineKeyboardButton('6Tignari', url='https://genshin-info.ru/wiki/personazhi/tignari/')
       btn177= types.InlineKeyboardButton('7Rayden', url='https://genshin-info.ru/wiki/personazhi/rayden/')
       keyboard.add(btn111, btn122, btn133, btn144, btn155, btn166, btn177)
       bot.send_message(message.from_user.id, 'Keyboard', reply_markup=keyboard)
    keyboard = types.InlineKeyboardMarkup()
    if message.text == '/oruzh':
        btn11 = types.InlineKeyboardButton('1kopya Homa', url='https://genshin-info.ru/wiki/oruzhie/kopya/posokh-khomy/')
        btn12 = types.InlineKeyboardButton('2tseremonialnyy-mech', url='https://genshin-info.ru/wiki/oruzhie/mechi/tseremonialnyy-mech/')
        btn13 = types.InlineKeyboardButton('3mech Kharan-geppaku-futsu',url='https://genshin-info.ru/wiki/oruzhie/mechi/kharan-geppaku-futsu/')
        btn14 = types.InlineKeyboardButton('4mech Omut',url='https://genshin-info.ru/wiki/oruzhie/mechi/dragotsennyy-omut/')
        btn15 = types.InlineKeyboardButton('5Dvuruk favonia',url='https://genshin-info.ru/wiki/oruzhie/dvuruchnye-mechi/dvuruchnyy-mech-favoniya/')
        btn16 = types.InlineKeyboardButton('6luk akva',url='https://genshin-info.ru/wiki/oruzhie/luki/akva-simulyakrum/')
        btn17 = types.InlineKeyboardButton('7prototip-zvyezdnyy-blesk',url='https://genshin-info.ru/wiki/oruzhie/kopya/prototip-zvyezdnyy-blesk/')
        keyboard.add(btn11, btn12, btn13, btn14, btn15, btn16, btn17)
        bot.send_message(message.from_user.id, 'Keyboard', reply_markup=keyboard)





bot.infinity_polling()