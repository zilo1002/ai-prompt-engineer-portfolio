from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path
import openai
import os

# -------------------
# 配置
# -------------------
app = FastAPI(title="AI Customer Support API")

# 默认 prompt 版本路径
PROMPT_DIR = Path("prompts")
DEFAULT_PROMPT = "v3_cot_temp0.3.json"

# 需要在 GitHub Secrets 或本地环境设置 OPENAI_API_KEY
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("请在环境变量设置 OPENAI_API_KEY")

# -------------------
# 数据模型
# -------------------
class Query(BaseModel):
    user_input: str
    prompt_version: str = DEFAULT_PROMPT  # 可选，v1/v2/v3

# -------------------
# 辅助函数
# -------------------
def load_prompt(version: str):
    prompt_path = PROMPT_DIR / version
    if not prompt_path.exists():
        raise ValueError(f"Prompt {version} 不存在")
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_json = json.load(f)
    system_prompt = prompt_json["role"] + "\n" + prompt_json["task"]
    return system_prompt, prompt_json.get("temperature", 0.3)

def call_openai(system_prompt: str, user_input: str, temperature: float):
    import openai
    openai.api_key = OPENAI_API_KEY
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature
    )
    return resp.choices[0].message.content

# -------------------
# 路由
# -------------------
@app.get("/")
def health_check():
    return {"status": "ok", "message": "AI Customer Support API is running"}

@app.post("/reply")
def generate_reply(query: Query):
    """
    输入：
      - user_input: 用户文本
      - prompt_version: 可选，选择 v1/v2/v3
    输出：
      - reply: LLM 回复
      - prompt_version: 实际使用的版本
    """
    system_prompt, temperature = load_prompt(query.prompt_version)
    reply = call_openai(system_prompt, query.user_input, temperature)
    return {
        "input": query.user_input,
        "reply": reply,
        "prompt_version": query.prompt_version
    }