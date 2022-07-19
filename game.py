from aiogram import types,Dispatcher


from config import  bot,ADMIN




# @dp.message_handler()
async def echo(message:types.Message):
   print(message)

   if message.from_user.id not in ADMIN:
       await message.answer('error')
   elif message.text.startswith('game'):
       await bot.send_dice(message.chat.id, emoji='🏀')


   elif message.text.isnumeric():

       message.text = int(message.text)
       await bot.send_message(message.chat.id, message.text **2)
   else:
       await bot.send_message(message.chat.id,message.text)

def register_handler_some(dp:Dispatcher):
    dp.register_message_handler(echo)