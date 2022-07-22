from aiogram import types,Dispatcher


from config import  bot ,ADMIN



async  def pin(message:types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer('eerror')
    elif message.text.startswith('game'):
        await bot.send_dice(message.chat.id, emoji='🏀')
    elif not message.reply_to_message:
        await message.answer('command must be reply')
    elif message.text.startswith('!pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)




def register_handlers_extra(dp:Dispatcher):
    dp.register_message_handler(pin)