from aiogram import types

kb_remove = types.ReplyKeyboardRemove()

kb_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_rf = types.KeyboardButton("Российский")
kb_zagran = types.KeyboardButton("Иностранный")
kb_start.add(kb_rf, kb_zagran)