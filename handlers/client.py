from aiogram import types,Dispatcher
from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton,ParseMode

from config import  bot,dp
from  keyboards import  client_kb
from database.bot_db import sql_random

# @dp.message_handler(commands=['questions'])
async def question_handler(message:types.Message):

    question = 'как перевести type с английского'
    answers = [
        'тип ','выбор','писать','привет'
    ]
    await bot.send_poll(
        chat_id= message.chat.id,
        question = question,
        options= answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='тип',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )

 async def pin(message:types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id,message.reply_message.message_id)
    else:
        await.message.reply('command must reply')

        
        
        
async  def show_random_user(message:types.Message):
    await sql_random(message)
    
        

async  def q_handler(message:types.Message):
    await  bot.send_message(message.from_user.id,f'text',reply_markup=client_kb.start_markup,)


# @dp.message_handler(commands=['meme'])
async def meme_handler(message:types.Message):
    media1 = open('media/img.png','rb')
    await bot.send_photo(message.from_user.id,photo=media1)


def register_handler_q(dp:Dispatcher):
    dp.register_message_handler(question_handler,commands=['questions1'])
    dp.register_message_handler(meme_handler,commands=['meme'])
    dp.register_message_handler(q_handler,commands=['questions'])
    dp.register_message_handler(pin,commands=['!pin'])
    dp.register_message_handler(show_random_user,commands=['random'])
        
