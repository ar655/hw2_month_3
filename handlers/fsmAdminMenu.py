from aiogram import types ,Dispatcher
from aiogram.dispatcher import FSMContext
from config import bot,ADMIN
from aiogram.dispatcher.filters.state import State,StatesGroup
from database import  bot_db
from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton








class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    dicript = State()
    price = State()

async def fsm_start(message:types.Message):
    if message.from_user.id not in ADMIN:
        await  message.answer('error')
    else:
        await FSMAdmin.photo.set()
        await message.answer('send food picture')

async  def load_photo(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('send food name')

async def load_name(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('send food discription')



async  def load_dicript(message:types.Message ,state :FSMContext):
    async with state.proxy() as data:
        data['discription'] = message.text
    await FSMAdmin.next()
    await message.answer('send food price')

async  def load_price(message:types.Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer('only numbers')
    else:
        async with state.proxy() as data:
            data['food price'] = message.text
            await bot.send_photo(message.from_user.id,data['photo'],
                                 caption=f"food name:{data['name']}\n"
                                         f"food discription:{data['discription']}\n"
                                         f"food price:{data['food price']}\n"
                                 )
    await state.finish()



async def delete_data(message:types.Message):
    if message.from_user.id in ADMIN and message.chat.type == 'private':
        foods = await bot_db.sql_command_all()
        for food in foods:
            await bot.send_photo(message.from_user.id, food[2],
                                 caption=f"food name:{food[3]}\n"
                                         f"food discription:{food[4]}\n"
                                         f"food price:{food[5]}\n",
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(
                                         f"delete: {food[3]}",
                                         callback_data=f"delete {food[3]}"

                                     )
                                 ))
    else:
        await message.reply('user id error')


async  def full_delete(call:types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace('delete',''))
    await call.answer(text='food has been deleted',show_alert=True)
    await bot.delete_message(call.message.chat.id,call.message.message_id)

def register_handlers_fsmAdminmenu(dp:Dispatcher):
    dp.register_message_handler(fsm_start,commands=['update_menu'])
    dp.register_message_handler(load_photo ,state=FSMAdmin.photo,content_types=['photo'])
    dp.register_message_handler(load_name,state=FSMAdmin.name)
    dp.register_message_handler(load_dicript,state=FSMAdmin.dicript)
    dp.register_message_handler(load_price,state=FSMAdmin.price)
    dp.register_message_handler(delete_data,commands=['del'])
    dp.register_callback_query_handler(full_delete,lambda call:call.data and call.data.startswith('delete'))





