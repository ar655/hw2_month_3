from aiogram import types,Dispatcher


from config import  bot ,ADMIN

import random 

async  def game(message:types.Message):
    if message.from_user.id  in ADMIN and  message.text.startswith('game') :
        emojis = ['🎯', '🎳', '🎰', '🎲', '⚽️', '️🏀']
        rand_mm  = random.choice(emojis)
        await bot.send_dice(message.chat.id , emoji=rand_mm)
    else:
        await message.answer('not admin')
    



def register_handlers_extra(dp:Dispatcher):
    dp.register_message_handler(game)
