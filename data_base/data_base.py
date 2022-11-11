import sqlite3 as sq
from create_bot import bot

base = sq.connect('./data_base/base.db')
cur = base.cursor()


def sql_start() -> None:
    base.execute('''CREATE TABLE IF NOT EXISTS users(id_user INT PRIMARY KEY, 
                                                     name TEXT, 
                                                     date_join TEXT, 
                                                     status INT DEFAULT 0, 
                                                     date_status TEXT DEFAULT 0, 
                                                     money TEXT DEFAULT 0)''')
    base.execute('''CREATE TABLE IF NOT EXISTS catalog(_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                       name TEXT, 
                                                       price TEXT, 
                                                       caption TEXT, 
                                                       photo_title TEXT, 
                                                       gallery TEXT, 
                                                       type_pack TEXT)''')
    base.commit()


async def add_user(id_user, name, date_join) -> None:
    cur.execute('INSERT INTO users(id_user, name, date_join) VALUES (?, ?, ?)', (id_user, name, date_join))
    base.commit()


async def add_photo(state) -> None:
    async with state.proxy() as data:
        cur.execute('''INSERT INTO catalog(name, price, caption, photo_title, gallery, type_pack) 
                       VALUES (?, ?, ?, ?, ?, ?)''', tuple(data.values()))
    base.commit()


async def data_user() -> dict:
    dict_users = {}
    for user in cur.execute('SELECT * FROM users').fetchall():
        dict_users[user[0]] = dict(zip(('name', 'date_join', 'status', 'date_status', 'money'), user[1:]))
    base.commit()
    return dict_users
