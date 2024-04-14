import aiosqlite
import sqlite3 as sq
import json
import os


async def sql_start_courier():
    base_a = sq.connect("data/courier.db")
    cur_a = base_a.cursor()
    
    if base_a:
        print("К базе данных курьеров произошло подключение")
        
    base_a.execute('''CREATE TABLE IF NOT EXISTS courier_data(id_users INTEGER,
                                                            citizenship TEXT,
                                                            name TEXT,
                                                            surname TEXT,
                                                            patronymic TEXT,
                                                            gender TEXT,
                                                            date_of_birth TEXT,
                                                            place_of_birth TEXT,
                                                            passport_issued TEXT,
                                                            passport_date_of_issue TEXT,
                                                            passport_department_code TEXT,
                                                            passport_series TEXT,
                                                            passport_number TEXT,
                                                            passport_registration TEXT,
                                                            passport_photo_main TEXT,
                                                            passport_photo_inhabitation TEXT,
                                                            passport_photo_face_main TEXT,
                                                            phone_number TEXT)''')
    base_a.commit()
    
    return


async def sql_start_storage_couriers():
    base_a = sq.connect("data/storage_couriers.db")
    cur_a = base_a.cursor()
    
    if base_a:
        print("К базе данных хранение курьеров произошло подключение")
        
    base_a.execute('''CREATE TABLE IF NOT EXISTS storage_data_couriers(id_users INTEGER,
                                                                        citizenship TEXT,
                                                                        name TEXT,
                                                                        surname TEXT,
                                                                        patronymic TEXT,
                                                                        gender TEXT,
                                                                        date_of_birth TEXT,
                                                                        place_of_birth TEXT,
                                                                        passport_issued TEXT,
                                                                        passport_date_of_issue TEXT,
                                                                        passport_department_code TEXT,
                                                                        passport_series TEXT,
                                                                        passport_number TEXT,
                                                                        passport_registration TEXT,
                                                                        passport_photo_main TEXT,
                                                                        passport_photo_inhabitation TEXT,
                                                                        passport_photo_face_main TEXT,
                                                                        phone_number TEXT)''')
    base_a.commit()
    
    return


async def sql_courier_add(id_users, citizenship, name, surname, patronymic, gender, date_of_birth, place_of_birth, passport_issued, passport_date_of_issue, passport_department_code, passport_series, passport_number, passport_registration, passport_photo_main, passport_photo_inhabitation, passport_photo_face_main, phone_number):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "courier.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        passport_photo_main = json.dumps(passport_photo_main)
        passport_photo_inhabitation = json.dumps(passport_photo_inhabitation)
        passport_photo_face_main = json.dumps(passport_photo_face_main)
        
        await cur.execute(f"INSERT INTO courier_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id_users, citizenship, name, surname, patronymic, gender, date_of_birth, place_of_birth, passport_issued, passport_date_of_issue, passport_department_code, passport_series, passport_number, passport_registration, passport_photo_main, passport_photo_inhabitation, passport_photo_face_main, phone_number))
        
        await db.commit()
        
        return


async def sql_delete_courier(id_user):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "courier.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        await cur.execute(f"DELETE FROM courier_data WHERE id_users = '{id_user}'")
        
        await db.commit()
        
        return
        
    
async def sql_id_courier():
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "courier.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute(f"SELECT id_users FROM courier_data GROUP BY id_users")
        id_user = await cur.fetchall()
        
        return id_user
    
    
async def sql_broadcast_data_couriers(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "courier.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute(f"SELECT * FROM courier_data WHERE id_users = '{id_users}'")
        courier_data = await cur.fetchall()
        
        await sql_storage_couriers_add(courier_data[0][0], courier_data[0][1], courier_data[0][2], courier_data[0][3], courier_data[0][4], courier_data[0][5], courier_data[0][6], courier_data[0][7], courier_data[0][8], courier_data[0][9], courier_data[0][10], courier_data[0][11], courier_data[0][12], courier_data[0][13], courier_data[0][14], courier_data[0][15], courier_data[0][16], courier_data[0][17])
    
    
async def sql_storage_couriers_add(id_users, citizenship, name, surname, patronymic, gender, date_of_birth, place_of_birth, passport_issued, passport_date_of_issue, passport_department_code, passport_series, passport_number, passport_registration, passport_photo_main, passport_photo_inhabitation, passport_photo_face_main, phone_number):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "storage_couriers.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        passport_photo_main = json.dumps(passport_photo_main)
        passport_photo_inhabitation = json.dumps(passport_photo_inhabitation)
        passport_photo_face_main = json.dumps(passport_photo_face_main)
        
        await cur.execute(f"INSERT INTO storage_data_couriers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id_users, citizenship, name, surname, patronymic, gender, date_of_birth, place_of_birth, passport_issued, passport_date_of_issue, passport_department_code, passport_series, passport_number, passport_registration, passport_photo_main, passport_photo_inhabitation, passport_photo_face_main, phone_number))
        
        await db.commit()
        
        return
    
    
async def sql_check_couriers(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "storage_couriers.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        await cur.execute(f"SELECT id_users FROM storage_data_couriers WHERE id_users == {str(id_users)}")
        user = await cur.fetchall()
        
        if user == []:
            
            return False
        
        else:
            
            return True