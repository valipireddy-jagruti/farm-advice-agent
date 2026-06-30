import sqlite3
import os

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "farm.db"
)

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ----------------------------------------------------
# Soil Table
# ----------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS soils (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    soil_name TEXT UNIQUE,
    ph REAL,
    drainage TEXT,
    fertility TEXT
)
""")

# ----------------------------------------------------
# Crop Table
# ----------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS crops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT,
    soil_name TEXT
)
""")

# ----------------------------------------------------
# Fertilizer Table
# ----------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS fertilizers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT,
    fertilizer TEXT
)
""")

# ----------------------------------------------------
# Disease Table
# ----------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS diseases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom TEXT,
    disease TEXT,
    treatment TEXT
)
""")

# ----------------------------------------------------
# Market Prices Table
# ----------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS market_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT,
    price TEXT
)
""")
#weather table
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    city TEXT PRIMARY KEY,
    weather TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")