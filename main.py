
from aiogram.utils import executor
from config import dp

import logging
import  asyncio
from handlers import  callback ,client , message,admin,fsmAdminMenu,notification
from database.bot_db import sql_create

client.register_handler_q(dp)
fsmAdminMenu.register_handlers_fsmAdminmenu(dp)



notification.register_func(dp)
callback.register_handlers_query(dp)


message.register_handler_some(dp)

admin.register_handlers_extra(dp)



async def on_startup(_)
    asyncio.create_task(notification.scheduler())
    sql_create()




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)
