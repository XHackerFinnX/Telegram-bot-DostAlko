import re
import aiosqlite
import sqlite3 as sq
import time
import datetime
import os


async def sql_start_courier_change():
    base_a = sq.connect("data/courier_change.db")
    cur_a = base_a.cursor()
    
    if base_a:
        print("К базе данных курьеров смены произошло подключение")
        
    base_a.execute('''CREATE TABLE IF NOT EXISTS courier_change_data(id_users INTEGER,
                                                                    name TEXT,
                                                                    surname TEXT,
                                                                    patronymic TEXT,
                                                                    day INTEGER,
                                                                    month INTEGER,
                                                                    hour INTEGER,
                                                                    minutes INTEGER,
                                                                    status TEXT)''')
    base_a.commit()
    
    return


async def sql_change_courier(id_users, name, surname, patronymic, day, month, hour, minutes, status):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "courier_change.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        await cur.execute(f"INSERT INTO courier_change_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (id_users, name, surname, patronymic, day, month, hour, minutes, status))
        
        await db.commit()
        
        return
    

async def write_courier_change_open(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "storage_couriers.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        await cur.execute(f"SELECT id_users, name, surname, patronymic FROM storage_data_couriers WHERE id_users == {str(id_users)}")
        user = await cur.fetchall()
        
        seconds = time.time()
        result = time.localtime(seconds)
        
        day = result.tm_mday
        month = result.tm_mon
        hour = result.tm_hour
        minutes = result.tm_min
        
        status = "Открыта"
        
        if await check_open_change_courier(id_users):
            pass
        
        else:
            
            return False
        
        await sql_change_courier(id_users, user[0][1], user[0][2], user[0][3], day, month, hour, minutes, status)
        
        return True
    
    
async def write_courier_change_close(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "storage_couriers.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        await cur.execute(f"SELECT id_users, name, surname, patronymic FROM storage_data_couriers WHERE id_users == {str(id_users)}")
        user = await cur.fetchall()
        
        seconds = time.time()
        result = time.localtime(seconds)
        
        day = result.tm_mday
        month = result.tm_mon
        hour = result.tm_hour
        minutes = result.tm_min
        
        status = "Закрыта"
        
        if await check_close_change_courier(id_users):
            pass
        
        else:
            
            return False
        
        await sql_change_courier(id_users, user[0][1], user[0][2], user[0][3], day, month, hour, minutes, status)
        
        return True
    

async def check_open_change_courier(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "courier_change.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        await cur.execute(f"SELECT status FROM courier_change_data WHERE id_users == {str(id_users)}")
        len_s = await cur.fetchall()
        
        if len(len_s) % 2 == 0:
            
            return True
        
        else:
            
            return False
        

async def check_close_change_courier(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "courier_change.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        await cur.execute(f"SELECT status FROM courier_change_data WHERE id_users == {str(id_users)}")
        len_s = await cur.fetchall()
        
        if len(len_s) % 2 == 0:
            
            return False
        
        else:
            
            return True