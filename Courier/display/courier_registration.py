from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keybord_markup.keybord import remove_keyboard, rf_or_zagran, check_yes_and_no, gender_m_g
from data.data_users import sql_users_add
from data.data_courier import sql_courier_add
from config.config import TOKENC, id_data_courier
from config.week import day_week
import time
import datetime

bot = Bot(token=TOKENC)

class RegistrationCourier(StatesGroup):
    
    citizenship = State()
    name = State()
    surname = State()
    patronymic = State()
    gender = State()
    date_of_birth = State()
    place_of_birth = State()
    passport_issued = State()
    passport_date_of_issue = State()
    passport_department_code = State()
    passport_series = State()
    passport_number = State()
    passport_registration = State()
    passport_photo_main = State()
    passport_photo_inhabitation = State()
    passport_photo_face_main = State()
    phone_number = State()


async def registration_citizenship(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['citizenship'] = message.text
        
        await RegistrationCourier.name.set()
        await message.answer(text= "Ваше имя:", reply_markup= await remove_keyboard())
        
        
async def registration_name(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['name'] = message.text
        
        await RegistrationCourier.surname.set()
        await message.answer(text= "Ваша фамилия:")
        
        
async def registration_surname(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['surname'] = message.text
        
        await RegistrationCourier.patronymic.set()
        await message.answer(text= "Ваше отчество:")
        
        
async def registration_patronymic(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['patronymic'] = message.text
        
        await RegistrationCourier.gender.set()
        await message.answer(text= "Пол:", reply_markup= await gender_m_g())
        
        
async def registration_gender(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['gender'] = message.text
        
        await RegistrationCourier.date_of_birth.set()
        await message.answer(text= "Дата рождения:", reply_markup= await remove_keyboard())
        

async def registration_date_of_birth(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['date_of_birth'] = message.text
        
        await RegistrationCourier.place_of_birth.set()
        await message.answer(text= "Место рождения:")
        

async def registration_place_of_birth(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['place_of_birth'] = message.text
        
        await RegistrationCourier.passport_issued.set()
        await message.answer(text= "Где выдан паспорт:")
        

async def registration_passport_issued(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['passport_issued'] = message.text
        
        await RegistrationCourier.passport_date_of_issue.set()
        await message.answer(text= "Дата выдачи паспорта:")
        

async def registration_passport_date_of_issue(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['passport_date_of_issue'] = message.text
        
        await RegistrationCourier.passport_department_code.set()
        await message.answer(text= "Код подразделения:")
        
        
async def registration_passport_department_code(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['passport_department_code'] = message.text
        
        await RegistrationCourier.passport_series.set()
        await message.answer(text= "Серия паспорта:")


async def registration_passport_series(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['passport_series'] = message.text
        
        await RegistrationCourier.passport_number.set()
        await message.answer(text= "Номер паспорта:")
        
        
async def registration_passport_number(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['passport_number'] = message.text
        
        await RegistrationCourier.passport_registration.set()
        await message.answer(text= "Место жительства (регистрация в паспорте):")
        
        
async def registration_passport_registration(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['passport_registration'] = message.text
        
        await RegistrationCourier.passport_photo_main.set()
        await message.answer(text= "Фото паспорта. Основной разворот (Фотография должна быть без бликов. Чтобы всё было чётко видеть!):")


async def registration_passport_photo_main(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['passport_photo_main'] = message.photo[0].file_id

        await RegistrationCourier.passport_photo_inhabitation.set()
        await message.answer(text= "Фото паспорта. Место жительства разворот (Фотография должна быть без бликов. Чтобы всё было чётко видеть!):")


async def registration_passport_photo_inhabitation(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['passport_photo_inhabitation'] = message.photo[0].file_id
        
        await RegistrationCourier.passport_photo_face_main.set()
        await message.answer(text= "Фото лица с паспортом. Основной разворот (Фотография должна быть без бликов. Чтобы всё было чётко видеть!):")


async def registration_passport_photo_face_main(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['passport_photo_face_main'] = message.photo[0].file_id
        
        await RegistrationCourier.phone_number.set()
        await message.answer(text= "Номер телефона:")
        

async def registration_phone_number(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['phone_number'] = message.text
        
        seconds = time.time()
        result = time.localtime(seconds)
        date = datetime.datetime(result.tm_year, result.tm_mon, result.tm_mday)
        
        data['day'] = await day_week(date.weekday())
        data['mday'] = str(result.tm_mday)
        data['mon_day'] = str(result.tm_mon)
        data['year_day'] = str(result.tm_year)
        
        id_user = str(message.chat.id)
        fname = str(message.from_user.first_name)
        lname = str(message.from_user.last_name)
        uname = '@' + str(message.from_user.username)
        
        list_photo = []
        list_photo.append(data['passport_photo_main'])
        list_photo.append(data['passport_photo_inhabitation'])
        list_photo.append(data['passport_photo_face_main'])
        
        media_photo = [types.InputMediaPhoto(list_photo[0], f"Заявка на работу курьера!\n"
                                                                                    f"{data['day']} {data['mday']:00}.{data['mon_day']:00}.{data['year_day']}\n"
                                                                                    f"Ник в тг: {fname} {lname} | {uname}\n"
                                                                                    f"Номер телефона: {data['phone_number']}\n"
                                                                                    f"Гражданство: {data['citizenship']}\n"
                                                                                    f"Имя: {data['name']}\n"
                                                                                    f"Фамилия: {data['surname']}\n"
                                                                                    f"Отчество: {data['patronymic']}\n"
                                                                                    f"Пол: {data['gender']}\n"
                                                                                    f"Дата рождения: {data['date_of_birth']}\n"
                                                                                    f"Место рождения: {data['place_of_birth']}\n"
                                                                                    f"Данные паспорта!\n"
                                                                                    f"Серия: {data['passport_series']} Номер: {data['passport_number']}\n"
                                                                                    f"Паспорт выдан: {data['passport_issued']}\n"
                                                                                    f"Дата выдачи: {data['passport_date_of_issue']}\n"
                                                                                    f"Код подразделения: {data['passport_department_code']}\n"
                                                                                    f"Место жительства: {data['passport_registration']}")]
        
        for i in list_photo:
            media_photo.append(types.InputMediaPhoto(i))
        media_photo.pop(1)
        
        await bot.send_media_group(id_data_courier, media_photo)
        sent_message_id = await bot.send_message(id_data_courier, "Принятие решение о рассмотрение заявки!", reply_markup= await check_yes_and_no(id_user))
        
        await sql_users_add(id_user, fname, lname, uname)
        
        await sql_courier_add(id_user, data['citizenship'], data['name'], data['surname'], data['patronymic'], data['gender'], data['date_of_birth'], data['place_of_birth'], data['passport_issued'], data['passport_date_of_issue'], data['passport_department_code'], data['passport_series'], data['passport_number'], data['passport_registration'], data['passport_photo_main'], data['passport_photo_inhabitation'], data['passport_photo_face_main'], data['phone_number'])
        
        await message.answer(text= "Заявка отправляна на рассмотрение! Ожидайте ответа.")
        
        sent_message_id = str(sent_message_id.message_id) # id сообщения
        
        list_photo = []
        await state.finish()
        
    
async def start_registration(dp: Dispatcher, message: types.Message):
    
    await RegistrationCourier.citizenship.set()
    await message.answer(text= "Какое у вас гражданство?", reply_markup= await rf_or_zagran())
    
    dp.register_message_handler(registration_citizenship, state=RegistrationCourier.citizenship)
    dp.register_message_handler(registration_name, state=RegistrationCourier.name)
    dp.register_message_handler(registration_surname, state=RegistrationCourier.surname)
    dp.register_message_handler(registration_patronymic, state=RegistrationCourier.patronymic)
    dp.register_message_handler(registration_gender, state=RegistrationCourier.gender)
    dp.register_message_handler(registration_date_of_birth, state=RegistrationCourier.date_of_birth)
    dp.register_message_handler(registration_place_of_birth, state=RegistrationCourier.place_of_birth)
    dp.register_message_handler(registration_passport_issued, state=RegistrationCourier.passport_issued)
    dp.register_message_handler(registration_passport_date_of_issue, state=RegistrationCourier.passport_date_of_issue)
    dp.register_message_handler(registration_passport_department_code, state=RegistrationCourier.passport_department_code)
    dp.register_message_handler(registration_passport_series, state=RegistrationCourier.passport_series)
    dp.register_message_handler(registration_passport_number, state=RegistrationCourier.passport_number)
    dp.register_message_handler(registration_passport_registration, state=RegistrationCourier.passport_registration)
    dp.register_message_handler(registration_passport_photo_main, content_types=['photo'], state=RegistrationCourier.passport_photo_main)
    dp.register_message_handler(registration_passport_photo_inhabitation, content_types=['photo'], state=RegistrationCourier.passport_photo_inhabitation)
    dp.register_message_handler(registration_passport_photo_face_main, content_types=['photo'], state=RegistrationCourier.passport_photo_face_main)
    dp.register_message_handler(registration_phone_number, state=RegistrationCourier.phone_number)