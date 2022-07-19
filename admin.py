from aiogram import types,Dispatcher


from config import  bot ,ADMIN



async  def pin(message:types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer('errorr')



    elif not message.reply_to_message:
        await  message.answer('command should be comment reply')
    elif message.text.startswith('!pin'):
        await bot.pin_chat_message(message.chat.id,message.message_id)

def register_handlers_extra(dp:Dispatcher):
    dp.register_message_handler(pin)