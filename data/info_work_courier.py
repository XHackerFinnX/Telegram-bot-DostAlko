import aiosqlite
import sqlite3 as sq
import json
import os


async def sql_start_courier():
    base_a = sq.connect("data/courier_info.db")
    cur_a = base_a.cursor()
    
    if base_a:
        print("К базе данных курьеров произошло подключение")
        
    base_a.execute('''CREATE TABLE IF NOT EXISTS courier_info_data(id_users INTEGER,
                                                                    balanc INTEGER,
                                                                    number_orders INTEGER,
                                                                    prize INTEGER,
                                                                    my_orders TEXT,
                                                                    work TEXT)''')
    base_a.commit()
    
    return