from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def menu(message):
    main = InlineKeyboardMarkup()
    signUp = InlineKeyboardButton(text='Kursga yozilish', callback_data='signUp')
    help = InlineKeyboardButton(text='Biz haqimizda', callback_data='help')
    main.add(signUp)
    main.add(help)
    return main

def signUpSend(message):
	main = InlineKeyboardMarkup()

	link_button = InlineKeyboardButton("Написать", url=f"tg://user?id={message.from_user.id}")

	main.add(link_button)
	return main

def about(message):
	main = InlineKeyboardMarkup()

	link_button = InlineKeyboardButton("Instagram 🔗", url=f"https://www.instagram.com/adm_invest_uz/")

	main.add(link_button)
	return main
