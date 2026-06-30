import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "farm.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ----------------------------
# Soil → Crop
# ----------------------------

crops = [
    ("black", "Cotton"),
    ("black", "Soybean"),
    ("black", "Sunflower"),
    ("black", "Sorghum"),
    ("black", "Wheat"),

    ("red", "Groundnut"),
    ("red", "Millets"),
    ("red", "Pulses"),

    ("clay", "Paddy"),
    ("clay", "Sugarcane"),

    ("sandy", "Groundnut"),
    ("sandy", "Watermelon"),
    ("sandy", "Coconut"),

    ("loamy", "Wheat"),
    ("loamy", "Maize"),
    ("loamy", "Tomato"),
    ("loamy", "Potato"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO crops(soil_name,crop_name) VALUES(?,?)",
    crops,
)

# ----------------------------
# Fertilizers
# ----------------------------

fertilizers = [
    ("Rice", "NPK 20-20-0"),
    ("Paddy", "Urea + DAP"),
    ("Cotton", "Potash + Urea"),
    ("Tomato", "Organic Compost + NPK"),
    ("Maize", "Nitrogen Rich Fertilizer"),
    ("Groundnut", "Gypsum + DAP"),
    ("Wheat", "NPK 10-26-26"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO fertilizers(crop_name,fertilizer) VALUES(?,?)",
    fertilizers,
)

# ----------------------------
# Diseases
# ----------------------------

diseases = [
    ("yellow leaves", "Nitrogen Deficiency", "Apply nitrogen fertilizer"),
    ("leaf spots", "Leaf Spot", "Use copper fungicide"),
    ("wilting", "Fusarium Wilt", "Improve drainage and apply fungicide"),
    ("white powder", "Powdery Mildew", "Apply sulfur fungicide"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO diseases(symptom,disease,treatment) VALUES(?,?,?)",
    diseases,
)

# ----------------------------
# Market Prices
# ----------------------------

prices = [
    ("Rice", "₹2500/quintal"),
    ("Cotton", "₹7200/quintal"),
    ("Tomato", "₹1800/quintal"),
    ("Maize", "₹2100/quintal"),
    ("Onion", "₹2400/quintal"),
    ("Groundnut", "₹6500/quintal"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO market_prices(crop_name,price) VALUES(?,?)",
    prices,
)

# ----------------------------
# Weather
# ----------------------------

weather = [
    ("Hyderabad", "29°C, Cloudy"),
    ("Secunderabad", "29°C, Cloudy"),
    ("Guntur", "32°C, Sunny"),
    ("Vijayawada", "31°C, Humid"),
    ("Warangal", "30°C, Partly Cloudy"),
    ("Karimnagar", "31°C, Sunny"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO weather(city,weather) VALUES(?,?)",
    weather,
)

conn.commit()
conn.close()

print("Database seeded successfully.")