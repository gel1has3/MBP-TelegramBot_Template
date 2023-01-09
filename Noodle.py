"""
This is a Atlantis Noodles bot.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types


# for reply keyboard (sends message)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from datetime import datetime


API_TOKEN = '5987897028:AAE8KDXmDnUqBJTN21m-iLaYCMtOcsFrt8g'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# get current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_hr = now.strftime("%H")
#print("Current Time =", current_hr)
#print("Current Time =", current_time)


answers = []  # store the answers they have given


# Menu selection
menu1 = KeyboardButton('Breakfast')
menu2 = KeyboardButton('Lunch')
menu3 = KeyboardButton('Dinner')
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    menu1).add(menu2).add(menu3)


# sends welcome message after start
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('I am Atlantis Noodles! Please select your menu', reply_markup=menu_kb)

# sends help message


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('I am Atlantis Noodles Bot and help your order. Press /start to get started. ')


# options selection: English
mnu_options1 = KeyboardButton('Atlantis Noodles 🍲')
mnu_options2 = KeyboardButton('Atlantis Pasta 🍛')
mnu_options3 = KeyboardButton('Atlantis Mojito 🍸')
mnu_options4 = KeyboardButton('Atlantis Grilled Chicken 🥠')
mnu_options_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    mnu_options1).add(mnu_options2).add(mnu_options3).add(mnu_options4)

# selecting what you need


@dp.message_handler(regexp='Breakfast')
async def Breakfast(message: types.Message):
    answers.append(message.text)
    await message.answer('What do you need?', reply_markup=mnu_options_kb)


@dp.message_handler(regexp='Lunch')
async def Lunch(message: types.Message):
    answers.append(message.text)
    await message.answer('What do you need?', reply_markup=mnu_options_kb)


@dp.message_handler(regexp='Dinner')
async def Dinner(message: types.Message):
    answers.append(message.text)
    await message.answer('What do you need?', reply_markup=mnu_options_kb)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer("Thanks for using Atlantis Noodles Bot 😁")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
