from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI(title="AI Customer Support API")

PROMPT_PATH = Path("prompts/v3_cot_temp0.3.json")

class Query(BaseModel):
    user_input: str

def load_prompt():
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        prompt = json.load(f)
    system_prompt = prompt["role"] + "\n" + prompt["task"]
    return system_prompt

SYSTEM_PROMPT = load_prompt()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "AI Customer Support API is running"}

@app.post("/reply")
def generate_reply(query: Query):
    """
    Mock version.
    Replace this part with real LLM API call later.
    """
    response = {
        "input": query.user_input,
        "reply": f"[MOCK RESPONSE] {query.user_input}",
        "prompt_version": PROMPT_PATH.name
    }
    return response