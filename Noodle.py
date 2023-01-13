"""
This is a Atlantis Noodles chatbot. The porgam is developed by
X code company. Copy right protected @2023.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types


# for reply keyboard (sends message)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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
# print("Current Time =", current_hr)
# print("Current Time =", current_time)


answers = []  # store the answers they have given


# Menu selection
menu1 = KeyboardButton('Breakfast')
menu2 = KeyboardButton('Lunch')
menu3 = KeyboardButton('Dinner')
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    menu1).add(menu2).add(menu3)

# menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
#    menu1, menu2, menu3)


# sends welcome message after start
# @dp.message_handler(commands=['start', 'help', 'hello', 'hi'])


@dp.message_handler(commands=['start', 'help', 'hello', 'hi'])
async def welcome(message: types.Message):
    await message.answer('I am Atlantis Noodles, and I am here to assist you with your order. Please pick your menu.', reply_markup=menu_kb)

# sends help message


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('I am Atlantis Noodles Bot and help your order. Press /start to get started. ')


# options selection: English
mnu_options1 = KeyboardButton('Atlantis Noodles 🍲')
mnu_options2 = KeyboardButton('Atlantis Pasta 🍛')
mnu_options3 = KeyboardButton('Atlantis Mojito 🍸')
mnu_options4 = KeyboardButton('Atlantis Grilled Chicken 🥠')
mnu_options5 = KeyboardButton('Atlantis SOUP')
mnu_options6 = KeyboardButton('Atlantis SALAD')
mnu_options7 = KeyboardButton('Atlantis Vegetable Corner')
mnu_options8 = KeyboardButton('Atlantis Smoothe')
mnu_options_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    mnu_options1).add(mnu_options2).add(mnu_options3).add(mnu_options4).add(mnu_options5).add(mnu_options6).add(mnu_options7).add(mnu_options8)


# Noodle options
Noodl1 = KeyboardButton('STIR FRY VEGETABLE NOODLE')
Noodl2 = KeyboardButton('STIR FRY FISH NOODLE')
Noodl3 = KeyboardButton('STIR FRY BEEF NOODLE')
Noodl4 = KeyboardButton('STIR FRY CHICKEN NOODLE')
Noodl5 = KeyboardButton('STIR FRY SPECIAL NOODLE')
Noodle_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    Noodl1).add(Noodl2).add(Noodl3).add(Noodl4).add(Noodl5)


# price list
order_options1 = KeyboardButton('Order')
order_options2 = KeyboardButton('Cancel')
order_options_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    order_options1).add(order_options2)


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


@dp.message_handler(commands=['pasta'])
async def pasta(message: types.Message):
    await message.answer_photo('https://t.me/atlantisnoodls/75')
    await message.answer('Your choice (የእርስዎ ምርጫ)', reply_markup=order_options_kb)


@dp.message_handler(regexp='Atlantis Pasta 🍛')
async def AtlantisPasta(message: types.Message):
    await message.answer_photo('https://t.me/atlantisnoodls/75')
    await message.answer('Your choice (የእርስዎ ምርጫ)', reply_markup=order_options_kb)


@dp.message_handler(regexp='Atlantis Noodles 🍲')
async def AtlantisNoodles(message: types.Message):
    await message.answer_photo('https://t.me/atlantisnoodls/63')
    await message.answer('Your choice (የእርስዎ ምርጫ)', reply_markup=Noodle_kb)


@dp.message_handler(regexp='Atlantis Mojito 🍸')
async def AtlantisMojito(message: types.Message):
    await message.answer_photo('https://t.me/atlantisnoodls/66')
    await message.answer_photo('https://t.me/atlantisnoodls/67')
    await message.answer('Your choice (የእርስዎ ምርጫ)', reply_markup=Noodle_kb)


@dp.message_handler(regexp='Atlantis Grilled Chicken 🥠')
async def AtlantisGrilledChicken(message: types.Message):
    await message.answer_photo('https://t.me/atlantisnoodls/68')
    await message.answer('Your choice (የእርስዎ ምርጫ)', reply_markup=Noodle_kb)


# Noodle familes
@dp.message_handler(regexp='STIR FRY VEGETABLE NOODLE')
async def vegetableNoodle(message: types.Message):
    await message.answer("The order STIR FRY VEGETABLE NOODLE has been chosen. Price $340", reply_markup=order_options_kb)


@dp.message_handler(regexp='STIR FRY FISH NOODLE')
async def fishNoodle(message: types.Message):
    await message.answer("The order STIR FRY FISH NOODLE has been chosen. Price $350", reply_markup=order_options_kb)


@dp.message_handler(regexp='STIR FRY BEEF NOODLE')
async def beefNoodle(message: types.Message):
    await message.answer("The order STIR FRY BEEF NOODLE has been chosen. Price $370", reply_markup=order_options_kb)


@dp.message_handler(regexp='STIR FRY CHICKEN NOODLE')
async def chickenNoodle(message: types.Message):
    await message.answer("The order STIR FRY CHICKEN NOODLE has been chosen. Price $380", reply_markup=order_options_kb)


@dp.message_handler(regexp='STIR FRY SPECIAL NOODLE')
async def specialNoodle(message: types.Message):
    await message.answer("The order STIR FRY SPECIAL NOODLE has been chosen. Price $410", reply_markup=order_options_kb)


@dp.message_handler(regexp='Order')
async def customer_order_response(message: types.Message):
    answers.append(message.text)
    await message.answer('Your order is processed. Thanks for chocing Atlantis chatbot. Follow the menu for more orders!!!', reply_markup=mnu_options_kb)


@dp.message_handler(regexp='Cancel')
async def customer_cancel_response(message: types.Message):
    answers.append(message.text)
    await message.answer('Your order is Cancel. Thanks for chocing Atlantis chatbot. To order again follow the menu', reply_markup=mnu_options_kb)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    # await message.answer("Thanks for using Atlantis Noodles Bot 😁")
    await message.answer('እኔ አትላንቲስ ኑድል chatbot ነኝ፣ እና በትዕዛዝዎ ላይ እርስዎን ለመርዳት እዚህ ነኝ። እባክዎን  ይምረጡ።', reply_markup=mnu_options_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
