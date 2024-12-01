import sqlite3

conn = sqlite3.connect('../../database/hometemp.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 1')
row = cursor.fetchone()
print(row)
conn.close()
