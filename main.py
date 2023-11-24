import logging
from aiogram import Bot, Dispatcher, types
from aiogram import executor

import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

admin_ids = [1244424464, 6735636743, 1592471406]


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if message.from_user.id not in admin_ids:
        await message.reply("Assalomu Alaykum!\n"
                            "Admin uchun habar qoldiring...")
    else:
        await message.reply("Assalomu Alaykum Admin!\n"
                            "Yangi xabarlarni kuting...")


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    if message.from_user.id in admin_ids:
        await bot.send_message(chat_id=message.from_user.id, text=f"{message.reply_to_message.text}"
                                                                  f"\n\nJavob:"
                                                                  f"\n{message.text}"
                                                                  f"\n\nYuborildi!")

        user_message = message.reply_to_message.text
        user_id = int(user_message.split()[0])
        await bot.send_message(chat_id=user_id, text=f"{message.reply_to_message.text}"
                                                     f"\n\nAdmin javobi:"
                                                     f"\n{message.text}")
    else:
        for admin_id in admin_ids:
            await bot.send_message(chat_id=admin_id, text=f"{message.from_user.id} "
                                                          f"\nusername: {message.from_user.full_name}"
                                                          f"\nnickname: @{message.from_user.username}"
                                                          f"\n\n{message.text}")
        await bot.send_message(chat_id=message.from_user.id,
                               text="Xabar adminga yuboildi.\nIltimos admin javobini kuting!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
