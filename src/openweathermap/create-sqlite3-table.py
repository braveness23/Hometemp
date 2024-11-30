import sqlite3

# Connect to the database
conn = sqlite3.connect('hometemp.db')
cursor = conn.cursor()

# Create the weather_data table
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    temperature REAL,
    feels_like REAL,
    humidity INTEGER,
    pressure INTEGER,
    wind_speed REAL,
    wind_deg INTEGER,
    weather_description TEXT
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
