from aiogram import Bot
from config.config import TOKENC
from keybord_markup.keybord import info_courier, change_open, change_close

bot = Bot(token=TOKENC)


async def work_courier_info(id_users):
    
    info_c = f"""
Баланс: {0} руб.\n
Кол-во заказов: {0}\n
Премия: {0} руб.
"""

    await bot.send_message(chat_id=id_users, text= info_c, reply_markup= await info_courier(id_users))