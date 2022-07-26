import asyncio
import aioschedule
from aiogram import  types,Dispatcher
from config import bot



async def get_chat_id(message:types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id,text='ok')


async def func():
    await bot.send_message(chat_id=chat_id,text='home-work')


async def scheduler():
    aioschedule.every().saturday.at('15:05').do(func)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_func(dp:Dispatcher):
    dp.register_message_handler(get_chat_id,lambda word:'h-w' in word.text )
