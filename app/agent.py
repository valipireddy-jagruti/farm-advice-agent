# ruff: noqa

import os
import json
import re
from datetime import datetime
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from app.database import (
    get_crops_by_soil,
    get_fertilizer,
    get_disease,
    get_market_price,
    get_weather as db_weather,
)
from app.knowledge import (
    save_crop,
    save_fertilizer,
    save_market_price,
    save_weather,
    save_disease,
)


load_dotenv()


# -------------------------------------------------------------------
# Environment
# -------------------------------------------------------------------

os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "False")

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# -------------------------------------------------------------------
# Security
# -------------------------------------------------------------------

PII_PATTERNS = [
    r"\b\d{12}\b",                    # Aadhaar
    r"\b\d{10}\b",                    # Phone
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
]

PROMPT_INJECTION_KEYWORDS = [
    "ignore previous instructions",
    "ignore all instructions",
    "system prompt",
    "developer message",
    "reveal prompt",
    "bypass",
    "jailbreak",
]


def scrub_pii(text: str) -> str:
    """Remove basic PII."""
    for pattern in PII_PATTERNS:
        text = re.sub(pattern, "[REDACTED]", text)
    return text


def detect_prompt_injection(text: str) -> bool:
    text = text.lower()
    return any(keyword in text for keyword in PROMPT_INJECTION_KEYWORDS)


def audit_log(event: str, severity: str = "INFO"):
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "severity": severity,
        "event": event,
    }
    print(json.dumps(log, indent=2))


# -------------------------------------------------------------------
# Tool Functions
# -------------------------------------------------------------------

def get_weather(location: str) -> str:
    weather = db_weather(location)

    if weather:
        return weather

    return f"No weather information available for {location}."



def crop_recommendation(soil: str) -> str:

    crops = get_crops_by_soil(soil)

    if crops:
        return (
            f"Recommended crops for {soil} soil:\n"
            + ", ".join(crops)
        )

    return (
        "DATABASE_MISS:"
        + soil
    )


def fertilizer_recommendation(crop: str) -> str:
    fertilizer = get_fertilizer(crop)

    if fertilizer:
        return fertilizer

    return f"No fertilizer recommendation found for {crop}."

def disease_detection(symptom: str) -> str:
    result = get_disease(symptom)

    if result:
        return (
            f"Disease: {result['disease']}\n"
            f"Treatment: {result['treatment']}"
        )

    return "Disease information not found."

def market_price(crop: str) -> str:
    price = get_market_price(crop)

    if price:
        return f"{crop.title()} price: {price}"

    return f"No market price available for {crop}."
# -------------------------------------------------------------------
# Shared Gemini Model
# -------------------------------------------------------------------

gemini_model = Gemini(
    model=MODEL_NAME,
    retry_options=types.HttpRetryOptions(
        attempts=3,
    ),
)
# -------------------------------------------------------------------
# Crop Advisor Agent
# -------------------------------------------------------------------

crop_agent = Agent(
    name="crop_advisor",
    model=gemini_model,
    instruction="""
You are an agricultural expert.

Help farmers with:
- Crop selection
- Soil suitability
- Irrigation advice
- Fertilizer recommendation
- Seasonal farming guidance

Always provide practical and easy-to-understand advice.
""",
    tools=[
        crop_recommendation,
        fertilizer_recommendation,
    ],
)

# -------------------------------------------------------------------
# Weather Advisor Agent
# -------------------------------------------------------------------

weather_agent = Agent(
    name="weather_advisor",
    model=gemini_model,
    instruction="""
You are a weather expert for agriculture.

Help farmers with:
- Current weather
- Irrigation planning
- Harvest planning
- Rainfall precautions
- Sowing recommendations

Always give practical and simple advice.
""",
    tools=[
        get_weather,
    ],
)
# -------------------------------------------------------------------
# Disease Advisor Agent
# -------------------------------------------------------------------

disease_agent = Agent(
    name="disease_advisor",
    model=gemini_model,
    instruction="""
You identify common crop diseases from symptoms.

Recommend:
- Possible disease
- Cause
- Treatment
- Prevention

If uncertain, clearly state that the diagnosis is only a suggestion.
""",
    tools=[
        disease_detection,
    ],
)

# -------------------------------------------------------------------
# Market Advisor Agent
# -------------------------------------------------------------------

market_agent = Agent(
    name="market_advisor",
    model=gemini_model,
    instruction="""
You help farmers sell crops profitably.

Provide:
- Market price
- Selling suggestions
- Storage advice
- Best selling time
""",
    tools=[
        market_price,
    ],
)

# -------------------------------------------------------------------
# Root Farm Advice Agent
# -------------------------------------------------------------------

root_agent = Agent(
    name="farm_advice_agent",
    model=gemini_model,
   instruction="""
You are an intelligent Farm Advice Assistant.

Always follow these rules.

1. Always use the available tools first.

2. If a tool returns useful information, use it.

3. If crop_recommendation returns DATABASE_MISS,
ignore that message and answer using your agricultural knowledge.

4. Never say:
- I don't know
- I don't have data
- I don't have information

Instead provide the best farming advice possible.

5. Explain answers in simple language for farmers.

6. If multiple questions are asked, combine all answers into one response.
""",
    tools=[
        get_weather,
        crop_recommendation,
        fertilizer_recommendation,
        disease_detection,
        market_price,
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)