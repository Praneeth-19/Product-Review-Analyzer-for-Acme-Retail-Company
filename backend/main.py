from fastapi import FastAPI, Form
import requests

app = FastAPI()

def query_ollama(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    # Print the response for debugging
    response_json = response.json()
    print("Ollama API Response:", response_json)
    
    # Check if 'response' key exists, otherwise look for alternative keys
    if "response" in response_json:
        return response_json["response"].strip()
    elif "text" in response_json:
        return response_json["text"].strip()
    elif "content" in response_json:
        return response_json["content"].strip()
    else:
        # Return the full response as a string if we can't find expected keys
        return str(response_json)

@app.post("/analyze/")
def analyze_review(text: str = Form(...)):
    sentiment_prompt = f"What is the sentiment (Positive, Neutral, Negative) of this review?\n\n{text}"
    topic_prompt = f"What is the main issue/topic discussed in this review?\n\n{text}"
    summary_prompt = f"Summarize the review in one short sentence:\n\n{text}"
    
    sentiment = query_ollama(sentiment_prompt)
    topic = query_ollama(topic_prompt)
    summary = query_ollama(summary_prompt)
    
    return {"sentiment": sentiment, "topic": topic, "summary": summary}