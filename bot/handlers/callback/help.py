from imports import *

@dp.callback_query_handler(text='help')
async def help(call: types.CallbackQuery):
    await bot.send_photo(call.from_user.id, photo='https://ic.wampi.ru/2023/07/21/image_2023-07-21_15-26-01.png', caption=f'{text.help(call)}', reply_markup=kbi.about(call))