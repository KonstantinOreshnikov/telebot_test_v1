from aiogram import Bot, types
from aiogram import Dispatcher as dp
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

bot = Bot(token='7047749443:AAF1JGuF0PItA5qpUGJYSHikUFoLlLZyJJw')
dp = dp(bot, storage=MemoryStorage())

# Словарь для хранения имен пользователей
user_data = {}

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    """
    Эта функция обрабатывает команду /start и отправляет приветственное сообщение.
    """
    await message.reply("Привет! Я ваш бот.")

# Команда /info
@dp.message_handler(commands=['info'])
async def info_command(message: types.Message):
    """
    Эта функция обрабатывает команду /info и отправляет информационное сообщение.
    """
    await message.reply("Я бот, созданный для помощи вам.")

# Команда /user_data
@dp.message_handler(commands=['user_data'])
async def user_data_command(message: types.Message):
    """
    Эта функция обрабатывает команду /user_data и отправляет данные о пользователе.
    """
    user_id = message.from_user.id
    if user_id in user_data:
        await message.reply(f"Ваше имя: {user_data[user_id]}")
    else:
        await message.reply("Я не знаю вашего имени.")

# Команда /echo
@dp.message_handler(commands=['echo'])
async def echo_command(message: types.Message):
    """
    Эта функция обрабатывает команду /echo и повторяет сообщение пользователя.
    """
    await message.reply(message.text[6:])

# Команда /remember_name
@dp.message_handler(commands=['remember_name'])
async def remember_name_command(message: types.Message):
    """
    Эта функция обрабатывает команду /remember_name и запоминает имя пользователя.
    """
    user_id = message.from_user.id
    user_name = message.text[15:]
    user_data[user_id] = user_name
    await message.reply(f"Я запомнил ваше имя: {user_name}")

# Команда /dice
@dp.message_handler(commands=['dice'])
async def dice_command(message: types.Message):
    """
    Эта функция обрабатывает команду /dice и отправляет эмодзи кубика.
    """
    dice_emoji = "🎲"
    await message.reply(dice_emoji)

if __name__ == '__main__':
    executor.start_polling(dp)