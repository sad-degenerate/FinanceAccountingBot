import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from dataBase import DataBase

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

db = DataBase("dataBase.db")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Hello, I'm bot finance accounting bot!")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    answer = "Available commands:\n"
    commands = config.AVAILABLE_COMMANDS
    count = 1

    for key in commands:
        answer += "{}. {} - {}\n".format(count, key, commands[key])
        count += 1

    await bot.send_message(message.from_user.id, answer)

@dp.message_handler(commands=['get_all_debts'])
async def get_all_debts(message: types.Message):
    debts = db.get_debts()
    answer = "All debts:\n" + "user_name \t\t debt\n"

    for debt in debts:
        answer += "{}\t\t{}\n".format(debt[0], str(debt[1]))

    await bot.send_message(message.from_user.id, answer)

@db.message_handler(commands=['set_debt'])
async def set_debt(message: types.Message):
    await bot.send_mesage(message.from_user.id, "test")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    db.close()