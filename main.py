from aiogram import executor
from data.config import dp

if __name__ == '__main__':
    from bot.handlers import *
    executor.start_polling(dp, skip_updates=True)
