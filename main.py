import asyncio
import logging
import sys
from os import getenv
import requests

from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = '6532793392:AAHAeSXVq80xHbeMyTm_3qxFQpfzFG34KRE'

dp = Dispatcher()
bot = Bot(token=TOKEN, parse_mode=ParseMode.MARKDOWN)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Напишите любое сообщение, чтобы получить его в ответ. Для завершения работы напишите /end.')


@dp.message(Command('end'))
async def end(message: Message):
    res = requests.post('https://jasik.alwaysdata.net/clear-ig-session', json={
        "contactId": f'{message.from_user.id}NEW_SULTAN'
    }, headers={'Content-Type': 'application/json'})
    await message.answer('Работа завершена.')
    await bot.close()


@ dp.message()
async def echo(message: Message):

    res = requests.post('https://jasik.alwaysdata.net/sultan-site', json={
        'message': message.text,
        "contactId": f'{message.from_user.id}NEW_SULTAN'
    }, headers={'Content-Type': 'application/json'})
    await message.answer(res.json()['message'])
