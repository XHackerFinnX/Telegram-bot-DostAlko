import aiosqlite
import sqlite3 as sq
import os
from config.current_time import time_day_mon

async def sql_start_users():
    base_a = sq.connect("data/users.db")
    cur_a = base_a.cursor()
    
    if base_a:
        print("К базе данных пользователей произошло подключение")
        
    base_a.execute('''CREATE TABLE IF NOT EXISTS users_data(id_users INTEGER,
                                                            fname TEXT,
                                                            lname TEXT,
                                                            uname TEXT,
                                                            day INTEGER,
                                                            month INTEGER)''')
    base_a.commit()
    
    return


async def sql_users_add(id_users, fname, lname, uname):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        await cur.execute(f"SELECT id_users, day, month FROM users_data WHERE id_users == {str(id_users)}")
        users = await cur.fetchall()
        
        day, month = await time_day_mon()
        
        if users == []:
            await cur.execute(f"INSERT INTO users_data VALUES (?, ?, ?, ?, ?, ?)", (id_users, fname, lname, uname, day, month))
            await db.commit()
            
            return
        
        await cur.execute(f"UPDATE users_data SET day = {day}, month = {month} WHERE id_users == {str(id_users)}")
        await db.commit()
        
        return
    
    
async def sql_users_check(id_users):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        await cur.execute(f"SELECT id_users, day, month FROM users_data WHERE id_users == {str(id_users)}")
        users = await cur.fetchall()
        
        if users == []:
            
            return True
        
        else:
            
            return False
        
        
async def sql_delete_users(id_user):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "users.db")
    async with aiosqlite.connect(db_path) as db:
        cur = await db.cursor()
        
        await cur.execute(f"DELETE FROM users_data WHERE id_users = '{id_user}'")
        
        await db.commit()
        
        return