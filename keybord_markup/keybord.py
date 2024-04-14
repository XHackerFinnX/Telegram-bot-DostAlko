import re
from turtle import width
from aiogram import types


async def remove_keyboard():
    kb_remove = types.ReplyKeyboardRemove()
    
    return kb_remove


async def rf_or_zagran():
    
    kb_rf_or_zagran = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_rf = types.KeyboardButton("Российский")
    kb_zagran = types.KeyboardButton("Иностранный")
    kb_rf_or_zagran.add(kb_rf, kb_zagran)
    
    return kb_rf_or_zagran


async def gender_m_g():
    
    kb_rf_or_zagran = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_m = types.KeyboardButton("Муж")
    kb_g = types.KeyboardButton("Жен")
    kb_rf_or_zagran.add(kb_m, kb_g)
    
    return kb_rf_or_zagran


async def check_yes_and_no(user_id):
    kb_yes_and_no = types.InlineKeyboardMarkup(resize_keyboard=True)
    kb_yes = types.InlineKeyboardButton("Принять", callback_data=f"YES_{user_id}")
    kb_no = types.InlineKeyboardButton("Отклонить", callback_data=f"NO_{user_id}")
    kb_yes_and_no.add(kb_yes, kb_no)
    
    return kb_yes_and_no


async def change_open():
    
    kb_change_o = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_open = types.KeyboardButton("Открыть смену")
    kb_change_o.add(kb_open)
    
    return kb_change_o


async def change_close():
    
    kb_change_c = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_close = types.KeyboardButton("Закрыть смену")
    kb_change_c.add(kb_close)
    
    return kb_change_c


async def info_courier(user_id):
    
    kb_info = types.InlineKeyboardMarkup(row_width= 2)
    kb_update = types.InlineKeyboardButton("Обновить данные", callback_data=f"UPDATE_{user_id}")
    kb_work_schedule = types.InlineKeyboardButton("График работы", callback_data=f"WORK_{user_id}")
    kb_help = types.InlineKeyboardButton("Поддержка", callback_data=f"HELP_{user_id}")
    kb_orders = types.InlineKeyboardButton("История заказов", callback_data=f"ORDERS_{user_id}")
    kb_info.add(kb_update, kb_work_schedule, kb_help, kb_orders)
    
    return kb_info
    