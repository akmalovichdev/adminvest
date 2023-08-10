from imports import *

class Info(StatesGroup):
    checkpass = State()
    adminka = State()
    rassilka = State()

@dp.message_handler(text="Админка")
async def admin(message: types.Message):
	if db.getUsersExist(message.chat.id) == True:
		await bot.send_message(message.chat.id, 'Введите пароль от админки', reply_markup=kbd.back())
		await Info.checkpass.set()

@dp.message_handler(state=Info.checkpass, content_types=types.ContentTypes.TEXT)
async def checkpass(message: types.Message, state: FSMContext):
	if message.text == 'Отмена':
		await bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=types.ReplyKeyboardRemove())
		await state.finish()
	else:
		adminpass = db.selectConf('adminpass')
		if message.text == adminpass:
			await bot.send_message(chat_id=message.chat.id, text='Вот ваше админ меню.', reply_markup = kbd.adminMenu())
			await Info.adminka.set()
		else:
			await bot.send_message(message.chat.id, 'Пароль не правильный\nПовторите попытку', reply_markup=kbd.back())
			await Info.checkpass.set()

@dp.message_handler(state=Info.adminka, content_types=types.ContentTypes.TEXT)
async def adminka(message: types.Message, state: FSMContext):
    if message.text.lower() == 'назад':
        await bot.send_message(chat_id=message.chat.id, text='Ты вернулся в главное меню.', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    elif message.text.lower() == 'рассылка':
        await bot.send_message(chat_id=message.chat.id, text='Введи текст для рассылки.', reply_markup=kbd.back())
        await state.finish()
        await Info.rassilka.set()
    elif message.text.lower() == 'статистика':
        all_users = db.getAllUsers()
        await bot.send_message(chat_id=message.chat.id, text=f'Пользователей в боте: {len(all_users)}', reply_markup = kbd.adminMenu())

@dp.message_handler(state=Info.rassilka, content_types=types.ContentTypes.ANY)
async def rassilka(message: types.Message, state: FSMContext):
	if message.text == 'Отмена':
		await bot.send_message(chat_id=message.chat.id, text='Ты вернулся в админ меню.', reply_markup=kbd.adminMenu())
		await state.finish()
		await Info.adminka.set()
	else:
		if types.ContentType.TEXT == message.content_type: # Если админ отправил текст
			start_time = time.time()
			users = db.getAllUsers()
			for user in users:
				try:
					await bot.send_message(chat_id=user[0], text=message.html_text, reply_markup=kbd.adminMenu())
					time.sleep(0.1)
				except:
					pass
			end_time = time.time()
			await bot.send_message(message.from_user.id, f"✔️ Рассылка успешно завершена за {round(end_time-start_time, 1)} сек. \n 》 Все пользователи получили ваше сообщение. 《", reply_markup=kbd.adminMenu())
			await state.finish()
			await Info.adminka.set()

		elif types.ContentType.PHOTO == message.content_type: # Если админ отправил фото
			start_time = time.time()
			users = db.getAllUsers()
			for user in users:
				try:
					await bot.send_photo(chat_id=user[0], photo=message.photo[-1].file_id, caption=message.html_text if message.caption else None, reply_markup=kbd.adminMenu())
					time.sleep(0.1)
				except:
					pass
			end_time = time.time()
			await bot.send_message(message.from_user.id, f"✔️ Рассылка успешно завершена за {round(end_time-start_time, 1)} сек. \n 》 Все пользователи получили ваше сообщение. 《", reply_markup=kbd.adminMenu())
			await state.finish()
			await Info.adminka.set()

		elif types.ContentType.VIDEO == message.content_type: # Если админ отправил видео
			start_time = time.time()
			users = db.getAllUsers()
			for user in users:
				try:
					await bot.send_video(chat_id=user[0], video=message.video.file_id, caption=message.html_text if message.caption else None, reply_markup=kbd.adminMenu())
					time.sleep(0.1)
				except:
					pass
			end_time = time.time()
			await bot.send_message(message.from_user.id, f"✔️ Рассылка успешно завершена за {round(end_time-start_time, 1)} сек. \n 》 Все пользователи получили ваше сообщение. 《", reply_markup=kbd.adminMenu())
			await state.finish()
			await Info.adminka.set()