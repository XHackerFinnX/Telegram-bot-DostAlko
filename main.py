from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiohttp.client_exceptions import ClientOSError, ClientConnectorError
from asyncio.exceptions import TimeoutError
from aiogram.utils.exceptions import MessageToDeleteNotFound, MessageCantBeDeleted, TelegramAPIError, NetworkError, RetryAfter
from config.config import TOKEN, admin
from data.data_users import sql_start_users, sql_users_check, sql_delete_users
from data.data_courier import sql_check_couriers
from data.data_courier import sql_start_courier, sql_start_storage_couriers, sql_id_courier, sql_delete_courier, sql_broadcast_data_couriers
from data.data_courier_change import sql_start_courier_change, write_courier_change_open, write_courier_change_close
from display.courier_registration import start_registration
from display.display_courier import work_courier_info
from keybord_markup.keybord import change_open, change_close
import asyncio

print("Бот запущен!")
print("DostAlkoСourier бот")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start", "update"])
async def start(message: types.Message):
    
    id_users = message.chat.id
    
    if message.chat.id in admin:
        
        await message.answer(text= "Добро пожаловать администратор!")
        
    else:
        
        await message.answer(text= "Добро пожаловать в DostAlkoСourier.")
        
        if await sql_users_check(id_users):
            
            await start_registration(dp, message)
            
        else:
            await bot.send_message(chat_id= id_users, text= 'Ваша информация о работе! Чтобы начать работу, нажмите "Открыть смену"!\nТакже вы можете проставить свой график работы, чтобы вам и нам было удобно отслеживать вашу активность на работе!', reply_markup= await change_open())
            await work_courier_info(id_users)


@dp.message_handler(text=["Открыть смену"])
async def open_close_change(message: types.Message):
    
    if await sql_check_couriers(message.chat.id):
        
        if await write_courier_change_open(message.chat.id):
            
            await message.answer(text= "Смена открыта! Удачной работы 👍", reply_markup= await change_close())
            
        else:
        
            await message.answer(text= "Открытие смены заблокировано! У вас уже открыта смена.")
            print("Открытие смены заблокировано! Открытая смена.")
        
    else:
        
        await message.answer(text= "Открытие смены заблокировано!")
        print("Открытие смены заблокировано!")
        
        
@dp.message_handler(text=["Закрыть смену"])
async def open_close_change(message: types.Message):
    
    if await sql_check_couriers(message.chat.id):
        
        if await write_courier_change_close(message.chat.id):
            
            await message.answer(text= "Смена закрыта!", reply_markup= await change_open())
            
        else:
        
            await message.answer(text= "Закрытие смены заблокировано! У вас уже закрыта смена.")
            print("Закрытие смены заблокировано! Закрыта смена.")
        
    else:
        
        await message.answer(text= "Закрытие смены заблокировано!")
        print("Закрытие смены заблокировано!")


@dp.callback_query_handler()
async def all_callback(callback: types.CallbackQuery):

    id_user = await sql_id_courier()
    # принятие заявки в курьеры
    try:
        
        for user in id_user:
            if callback.data == f"YES_{str(user[0])}":

                await bot.send_message(chat_id=user[0], text= "Заявка одобрена!")

                await sql_broadcast_data_couriers(user[0])
                await sql_delete_courier(user[0])
                
                await bot.send_message(chat_id= user[0], text= 'Ваша информация о работе! Чтобы начать работу, нажмите "Открыть смену"!\nТакже вы можете проставить свой график работы, чтобы вам и нам было удобно отслеживать вашу активность на работе!', reply_markup= await change_open())
                await work_courier_info(user[0])

            elif callback.data == f"NO_{str(user[0])}":

                await bot.send_message(chat_id=user[0], text= "Заявка отклонена!")

                await sql_delete_courier(user[0])
                await sql_delete_users(user[0])
    
    except:
        print("Ошибка с долгой отправкой на одобрение заявки!")
    
    # Запросы callback курьеров в их личном кабинете
    
    try:
        if callback.data == f"UPDATE_{callback.from_user.id}":
            await work_courier_info(callback.from_user.id)
        
    except:
        pass

async def main():
    
    await sql_start_users()
    await sql_start_courier()
    await sql_start_storage_couriers()
    await sql_start_courier_change()
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())