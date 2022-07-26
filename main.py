
from aiogram.utils import executor
from config import dp

import logging

from handlers import  callback ,client , message,admin,fsmAdminMenu
from database.bot_db import sql_create

fsmAdminMenu.register_handlers_fsmAdminmenu(dp)
client.register_handler_q(dp)
callback.register_handlers_query(dp)
admin.register_handlers_extra(dp)

message.register_handler_some(dp)



async def on_startup(_)
    sql_create()




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)
