from data.config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher import FSMContext
from data import db as db, text as text
from bot.keyboards import default as kbd, inline as kbi
import time
import schedule
import requests
import os.path
import logging
import asyncio
# logging.basicConfig(filename='bot.log', level=logging.)