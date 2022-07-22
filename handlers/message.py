from aiogram import types,Dispatcher


from config import  bot,ADMIN




# @dp.message_handler()
async def echo(message:types.Message):

   if message.text.isnumeric():

       message.text = int(message.text)
       await bot.send_message(message.chat.id, message.text **2)
   else:
       await bot.send_message(message.chat.id,message.text)

def register_handler_some(dp:Dispatcher):
    dp.register_message_handler(echo)
