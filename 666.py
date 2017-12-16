import telebot
from telebot import types

TOKEN = '<тутваштокен?'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add('Налево', 'Направо')
	
	msg = bot.send_message(m.chat.id, 'Привет, человек! Выбери путь:',
		reply_markup=keyboard)
	bot.register_next_step_handler(msg, put)
def put(m): # Нужно заменить, если у вас в def start указано другое
	if m.text == "Налево": # Нужно заменить, если у вас в def start указано другое
		bot.send_message(m.chat.id, 'Вы не нашли корзину')
	elif m.text == "Направо":
		bot.send_message(m.chat.id, 'Вы нашли корзину')
		
bot.polling()