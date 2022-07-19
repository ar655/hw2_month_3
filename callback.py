from aiogram import types,Dispatcher
from aiogram.types import ParseMode
from  config import bot


# @dp.callback_query_handler(command=['questions2'])
async def question_handler2(message:types.Message):



    question = 'как перевести if с английского '
    answers = [
        'если ','вчера','день','завтрак'
    ]
    await bot.send_poll(
        chat_id= message.chat.id,
        question = question,
        options= answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='если',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )


async def question_handler3(message:types.Message):


    question = 'как перевести but с английского '
    answers = [
        'но ','стул','почему','что'
    ]
    await bot.send_poll(
        chat_id= message.chat.id,
        question = question,
        options= answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='но',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )

def register_handlers_query(dp:Dispatcher):
    dp.register_message_handler(
        question_handler2 , commands=['questions2']
    )
    dp.register_message_handler(
        question_handler3,commands=['questions3']
    )