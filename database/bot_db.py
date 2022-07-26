import sqlite3
from config import bot ,ADMIN
from  aiogram import  types ,Dispatcher
import random



def sql_create():
    global db,cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()
    if db:
        print('data base connected')
    db.execute("CREATE TABLE IF NOT EXISTS menu"
               "(photo TEXT,"
               "name TEXT PRIMARY KEY,"
               "discription TEXT,"
               "food price INTEGER)")
    db.commit()

async def sql_insert_data(state):

    async with state.proxy() as data:
        cursor.execute("INSERT INTO menu VALUES"
                       "(?,?,?,?)",tuple(data.values()))
        db.commit()




async def sql_random(message):
    result = cursor.execute("SELECT * FROM  menu ").fetchall()
    random_food = random.choice(result)
    await bot.send_photo(message.from_user.id, random_food[2],
                         caption=f"food name:{random_food[3]}\n"
                                 f"food discription:{random_food[4]}\n"
                                 f"food price:{random_food[5]}\n"


                         )





async def sql_command_all():
    return  cursor.execute("SELECT * FROM  menu ").fetchall()




async  def sql_command_delete(name):
    cursor.execute("DELETE FROM menu WHERE name == ?", (name,))
    db.commit()






































