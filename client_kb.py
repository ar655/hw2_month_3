from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


start_button = KeyboardButton('H')
start_markup = ReplyKeyboardMarkup()
start_markup.row(start_button)

q_button1 = KeyboardButton('/questions1')
q_button2 = KeyboardButton('/questions2')
q_button3 = KeyboardButton('/questions3')

start_markup =ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.row(q_button1,q_button2,q_button3)






