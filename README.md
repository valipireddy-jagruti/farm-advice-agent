# 🌾 Farm AI Assistant
<img width="768" height="512" alt="agent_workflow" src="https://github.com/user-attachments/assets/65c6c8da-071e-4b5f-be36-189d50b067f4" />



An AI-powered Farm Advice Assistant built using **Google Agent Development Kit (ADK)** and **Gemini 2.5 Flash**.

The assistant helps farmers make informed agricultural decisions by providing crop recommendations, fertilizer suggestions, disease diagnosis, weather updates, and market prices through natural language conversations.

---

## 📸 Dashboard

<img width="560" height="841" alt="farm_ai_home_page" src="https://github.com/user-attachments/assets/f3959a83-9cef-49d4-bbbc-ab693e3a2379" />



---

## ✨ Features

- 🌱 Crop recommendations based on soil type
- 🌾 Fertilizer recommendations for different crops
- 🌦️ Weather information for farming decisions
- 🦠 Crop disease identification and treatment suggestions
- 📈 Market price lookup for agricultural products
- 💬 Natural language conversation using Gemini AI
- 🗄️ SQLite knowledge base for structured agricultural data
- 🔄 Automatic fallback to Gemini when database information is unavailable

---

## 🛠️ Tech Stack
<img width="768" height="512" alt="tech_stack" src="https://github.com/user-attachments/assets/73a5a6a3-0e63-4769-b48c-c7380270f5ab" />

- Python 3.13
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash
- SQLite
- FastAPI
- Agents CLI
- UV Package Manager

---

## 📂 Project Structure

```text
farm-advice-agent/
│
├── app/
│   ├── agent.py               # Main Farm AI Agent
│   ├── database.py            # SQLite database functions
│   ├── knowledge.py           # Knowledge storage utilities
│   ├── fallback.py            # Gemini fallback logic
│   └── fast_api_app.py        # FastAPI backend
│
├── data/
│   └── farm.db                # SQLite knowledge database
│
├── scripts/
│   ├── init_database.py       # Create database tables
│   └── seed_database.py       # Insert sample agricultural data
│
├── tests/
├── deployment/
├── pyproject.toml
└── README.md
```
<img width="768" height="512" alt="system_architecture" src="https://github.com/user-attachments/assets/6eb7c3f1-8279-409c-a03b-f410b6dbd6b2" />


---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/valipireddy-jagruti/farm-advice-agent.git

cd farm-advice-agent
```

Install dependencies

```bash
agents-cli install
```

---

## ⚙️ Configure Environment

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

---

## 🗄️ Initialize Database

Create the SQLite database

```bash
uv run python scripts/init_database.py
```

Seed sample agricultural data

```bash
uv run python scripts/seed_database.py
```

---

## ▶️ Run the Project

Start the development playground

```bash
agents-cli playground
```

or

```bash
uv run python app/fast_api_app.py
```

---

## 💬 Example Queries

- Recommend crops for black soil
- Best fertilizer for cotton
- Weather in Hyderabad
- Disease causing yellow leaves in rice
- Market price of tomato
- Can I grow wheat during rainy season?

---

## 🧠 How It Works

1. User submits a farming-related question.
2. The ADK agent identifies the user's intent.
3. Relevant tool functions query the SQLite knowledge base.
4. If information exists, it is returned immediately.
5. If no record exists, Gemini generates an intelligent response.
6. New knowledge can optionally be stored in the database for future use.

---

## 📊 Database
<img width="768" height="512" alt="database_schema" src="https://github.com/user-attachments/assets/a60919d0-b3c2-46a4-bedd-cdce23d14f5c" />

SQLite stores structured agricultural knowledge including:

- Soil types
- Crop recommendations
- Fertilizers
- Diseases
- Weather information
- Market prices

---

## 🔮 Future Improvements

- Real-time weather API integration
- Live market prices
- Voice assistant support
- Regional language support
- Image-based crop disease detection
- Vector database integration for semantic search
- RAG using Vertex AI Search or ChromaDB

---

## 👩‍💻 Author

**Jagruti Vallipireddy**

GitHub:
https://github.com/valipireddy-jagruti

---

## 📄 License

This project is developed for educational and learning purposes.
