import re

from app.knowledge import (
    save_crop,
    save_fertilizer,
    save_market_price,
    save_weather,
)


def learn_crop(soil: str, gemini_answer: str):
    """
    Save crops returned by Gemini into SQLite.
    """

    crops = re.split(r",|\n", gemini_answer)

    crops = [
        crop.strip(" .")
        for crop in crops
        if len(crop.strip()) > 2
    ]

    if crops:
        save_crop(soil, crops)


def learn_fertilizer(crop: str, answer: str):
    save_fertilizer(crop, answer)


def learn_market_price(crop: str, answer: str):
    save_market_price(crop, answer)


def learn_weather(city: str, answer: str):
    save_weather(city, answer)