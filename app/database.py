import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "farm.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


# ---------------------------------------------------
# Crop Recommendations
# ---------------------------------------------------

def get_crops_by_soil(soil):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT crop_name
        FROM crops
        WHERE LOWER(soil_name)=LOWER(?)
    """, (soil,))

    rows = cur.fetchall()
    conn.close()

    return [r[0] for r in rows]


# ---------------------------------------------------
# Fertilizers
# ---------------------------------------------------

def get_fertilizer(crop):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT fertilizer
        FROM fertilizers
        WHERE LOWER(crop_name)=LOWER(?)
    """, (crop,))

    row = cur.fetchone()
    conn.close()

    if row:
        return row[0]

    return None


# ---------------------------------------------------
# Diseases
# ---------------------------------------------------

def get_disease(symptom):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT disease,treatment
        FROM diseases
        WHERE LOWER(symptom)=LOWER(?)
    """, (symptom,))

    row = cur.fetchone()
    conn.close()

    if row:
        return {
            "disease": row[0],
            "treatment": row[1]
        }

    return None


# ---------------------------------------------------
# Market Prices
# ---------------------------------------------------

def get_market_price(crop):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT price
        FROM market_prices
        WHERE LOWER(crop_name)=LOWER(?)
    """, (crop,))

    row = cur.fetchone()
    conn.close()

    if row:
        return row[0]

    return None


# ---------------------------------------------------
# Weather
# ---------------------------------------------------

def get_weather(city):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT weather
        FROM weather
        WHERE LOWER(city)=LOWER(?)
    """, (city,))

    row = cur.fetchone()
    conn.close()

    if row:
        return row[0]

    return None