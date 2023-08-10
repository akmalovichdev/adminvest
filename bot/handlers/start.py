from imports import *
from ..states.register import UserForm

@dp.message_handler()
async def start(message: types.Message):
    if not db.getUsersExist(message.from_user.id):
        await UserForm.fullname.set()
        await bot.send_message(message.chat.id, f'{text.start(message)}')
        return
    
    await bot.send_message(message.chat.id, f'{text.start(message)}', reply_markup=kbi.menu(message))

@dp.message_handler(state=UserForm.fullname, content_types=types.ContentTypes.TEXT)
async def fullname(message: types.Message, state: FSMContext):
    errorname = message.text.isalpha()
    if errorname == False or len(message.text) <= 3:
        await bot.send_message(message.chat.id, f'{text.register.userNameError(message)}')
    else:
        await state.update_data(userName = message.text)
        await bot.send_message(message.chat.id, f'{text.register.sendContact(message)}', reply_markup=kbd.sendContact(message))
        await UserForm.contact.set()

@dp.message_handler(state=UserForm.contact, content_types=types.ContentTypes.ANY)
async def contact(message: types.Message, state: FSMContext):
    if message.contact:
        if message.contact.phone_number[0] == "+":
            phonen = message.contact.phone_number
        else:
            phonen = '+' + str(message.contact.phone_number)
        data = await state.get_data()

        db.adduser(message.from_user.id, data['userName'], phonen)

        await bot.send_photo(message.chat.id, photo='https://im.wampi.ru/2023/07/21/image_2023-07-21_15-26-07.png', caption=f'{text.register.registerSuccess(message)}', reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(message.chat.id, f'{text.start(message)}', reply_markup=kbi.menu(message))
        await state.finish()
    else:
        await bot.send_message(message.chat.id, f'{text.register.sendContact(message)}', reply_markup=kbd.sendContact(message))
        await UserForm.contact.set()
