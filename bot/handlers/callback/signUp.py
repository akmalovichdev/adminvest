from imports import *

@dp.callback_query_handler(text='signUp')
async def signUp(call: types.CallbackQuery):
    await bot.send_photo(call.from_user.id, photo='https://ie.wampi.ru/2023/07/21/image_2023-07-21_15-25-53.png', caption=f'{text.signUp(call)}')
    await bot.send_message(-864765218, f'{text.signUpSend(call)}', reply_markup=kbi.signUpSend(call))

