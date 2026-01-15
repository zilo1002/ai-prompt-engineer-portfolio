import requests

url = "http://127.0.0.1:8000/reply"

examples = [
    {"user_input": "My package is late", "prompt_version": "v2_shot3_temp0.3.json"},
    {"user_input": "The item arrived damaged", "prompt_version": "v3_cot_temp0.3.json"}
]

for ex in examples:
    resp = requests.post(url, json=ex)
    print(f"Input: {ex['user_input']}")
    print(f"Reply: {resp.json()['reply']}")
    print(f"Prompt version: {resp.json()['prompt_version']}")
    print("-" * 30)