import sqlite3
conn = sqlite3.connect('ekz_sql.db')
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tabla (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     planet text,
#     number_pl int)''')
cursor.execute('''INSERT INTO tabla (planet, number_pl) VALUES 
    ("MERCURY", 1),
    ("VENUS", 2),
    ("EARTH", 3),
    ("MARS", 4)''')
conn.commit()
cursor.close()