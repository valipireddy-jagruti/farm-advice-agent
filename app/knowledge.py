import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "farm.db"


def save_crop(soil, crops):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for crop in crops:
        cur.execute("""
            INSERT OR IGNORE INTO crops
            (soil_name, crop_name)
            VALUES (?, ?)
        """, (soil.lower(), crop.strip()))

    conn.commit()
    conn.close()


def save_fertilizer(crop, fertilizer):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT OR REPLACE INTO fertilizers
        (crop_name, fertilizer)
        VALUES (?, ?)
    """, (crop.lower(), fertilizer))

    conn.commit()
    conn.close()


def save_market_price(crop, price):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT OR REPLACE INTO market_prices
        (crop_name, price)
        VALUES (?, ?)
    """, (crop.lower(), price))

    conn.commit()
    conn.close()


def save_weather(city, weather):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT OR REPLACE INTO weather
        (city, weather)
        VALUES (?, ?)
    """, (city.lower(), weather))

    conn.commit()
    conn.close()


def save_disease(symptom, disease, treatment):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT OR REPLACE INTO diseases
        (symptom, disease, treatment)
        VALUES (?, ?, ?)
    """, (symptom.lower(), disease, treatment))

    conn.commit()
    conn.close()