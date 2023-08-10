from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

###############################################################################################################################################################

def adminMenu():
	button1 = KeyboardButton('Статистика')
	button2 = KeyboardButton('Рассылка')
	button3 = KeyboardButton('Назад')
	admin1_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	admin1_kb.add(button1)
	admin1_kb.add(button2)
	admin1_kb.add(button3)
	return admin1_kb
	
def back():
	back_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	button = KeyboardButton('Bekor qilish')
	back_kb1.add(button)
	return back_kb1

def sendContact(message):
	main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	share_contact = KeyboardButton("Kontaktingizni yuboring ☎️", request_contact=True)
	main.add(share_contact)
	return main

