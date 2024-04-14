from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

print("Бот запущен!")
print("DostAlko бот")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    
    await message.answer(text= "Добро пожаловать в DostAlko.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)