import requests
import datetime
from config import tg_boten_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot=Bot(token=tg_boten_token)
dp=Dispatcher(bot)


@dp.message_handlers(commands=["starts"])
async def start_command(message: types.Message):
    await message.reply ("Привет напиши мне название города и я пришлю сводку")


if __name__=='__main__':
    executor.start_polling(dp)