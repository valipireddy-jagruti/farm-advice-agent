# 🌾 Farm AI Assistant

<img width="768" height="512" alt="agent_workflow" src="https://github.com/user-attachments/assets/65c6c8da-071e-4b5f-be36-189d50b067f4" />

An AI-powered Farm Advice Assistant built using **Google Agent Development Kit (ADK)** and **Gemini 2.5 Flash**.

The assistant helps farmers make informed agricultural decisions by providing crop recommendations, fertilizer suggestions, disease diagnosis, weather updates, and market prices through natural language conversations.

---

# ✨ Features

- 🌱 Crop recommendations based on soil type
- 🌾 Fertilizer recommendations for different crops
- 🌦️ Weather information for farming decisions
- 🦠 Crop disease identification and treatment suggestions
- 📈 Market price lookup for agricultural products
- 💬 Natural language conversation using Gemini AI
- 🗄️ SQLite knowledge base for structured agricultural data
- 🔄 Automatic fallback to Gemini when database information is unavailable

---

# 🛠 Tech Stack

<img width="768" height="512" alt="tech_stack" src="https://github.com/user-attachments/assets/73a5a6a3-0e63-4769-b48c-c7380270f5ab" />

- Python 3.13
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash
- SQLite
- FastAPI
- Agents CLI
- UV Package Manager

---

# 🏗 System Architecture

<img width="768" height="512" alt="system_architecture" src="https://github.com/user-attachments/assets/6eb7c3f1-8279-409c-a03b-f410b6dbd6b2" />

### Workflow

1. User submits a farming-related question.
2. ADK Agent understands the request.
3. Appropriate tool is selected.
4. SQLite database is queried.
5. If data exists, it is returned.
6. Otherwise Gemini generates an intelligent response.
7. The response is shown to the user.
8. New knowledge can optionally be stored for future use.

---

# 📸 Dashboard

<img width="560" height="841" alt="farm_ai_home_page" src="https://github.com/user-attachments/assets/f3959a83-9cef-49d4-bbbc-ab693e3a2379" />

---

# 📊 Database Design

<img width="768" height="512" alt="database_schema" src="https://github.com/user-attachments/assets/a60919d0-b3c2-46a4-bedd-cdce23d14f5c" />

SQLite stores structured agricultural knowledge including:

- Soil Types
- Crop Recommendations
- Fertilizers
- Diseases
- Weather Information
- Market Prices

---

# 📂 Project Structure

```text
farm-advice-agent/
│
├── app/
│   ├── agent.py
│   ├── database.py
│   ├── knowledge.py
│   ├── fallback.py
│   └── fast_api_app.py
│
├── data/
│   └── farm.db
│
├── scripts/
│   ├── init_database.py
│   └── seed_database.py
│
├── tests/
├── deployment/
├── pyproject.toml
└── README.md
```

---

# 🚀 Installation

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

# ⚙ Configuration

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

---

# 🗄 Initialize Database

Create the database

```bash
uv run python scripts/init_database.py
```

Seed agricultural data

```bash
uv run python scripts/seed_database.py
```

---

# ▶ Run the Project

Start the playground

```bash
agents-cli playground
```

or

```bash
uv run python app/fast_api_app.py
```

---

# 💬 Example Queries

```
Recommend crops for black soil
```

```
Best fertilizer for cotton
```

```
Weather in Hyderabad
```

```
Disease causing yellow leaves in rice
```

```
Market price of tomato
```

```
Can I grow wheat during rainy season?
```

---
output:
<img width="1920" height="1080" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/4413a8ab-37e0-4779-b2f3-1cc6e89d092e" />
<img width="1920" height="1080" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/1ea6d9fa-a391-474d-b4fe-34fc27f8101a" />


# 🔮 Future Improvements

- Live Weather API Integration
- Live Market Price APIs
- Voice-based Assistant
- Regional Language Support
- Image-based Disease Detection
- Vector Database Integration
- RAG using Vertex AI Search / ChromaDB
- Cloud Deployment

---

# 👩‍💻 Author

**Jagruti Vallipireddy**

GitHub:
https://github.com/valipireddy-jagruti

---

# 📄 License

This project is developed for educational and learning purposes.
