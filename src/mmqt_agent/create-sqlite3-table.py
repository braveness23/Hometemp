import sqlite3

# Initialize the database
conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

# Create a table for temperature readings
cursor.execute('''
CREATE TABLE IF NOT EXISTS temperature_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    temperature REAL
)
''')
conn.commit()
conn.close()