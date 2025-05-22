# Acme Product Review Analyzer
An AI-powered tool that analyzes customer reviews for sentiment, topic, and support, and logistics.
## Features
- Upload CSVs of product reviews
- Automatically classify sentiment (Positive, Neutral, Negative)
- Detect key topics (e.g., delivery, quality)
- Generate a one-line summary
- Download results or explore them on an interactive dashboard
## Stack

- LLM: Mistral via Ollama
- Backend: FastAPI
- Frontend: Streamlit
- Visualization: Altair/Streamlit Charts
## Run
1. Pull model: `ollama pull mistral`
2. Run backend: `uvicorn backend.main:app --reload`
3. Run frontend: `streamlit run frontend/app.py`
