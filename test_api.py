import requests

# 本地 FastAPI 服务地址
API_URL = "http://127.0.0.1:8000/reply"

# 测试示例
examples = [
    {"user_input": "My package hasn't arrived and no one replied.", "prompt_version": "v1_shot0_temp0.7.json"},
    {"user_input": "The item arrived broken and I'm very frustrated.", "prompt_version": "v2_shot3_temp0.3.json"},
    {"user_input": "Why was I charged extra customs fees?", "prompt_version": "v3_cot_temp0.3.json"}
]

def test_api():
    print("=== Testing AI Customer Support API ===\n")
    for ex in examples:
        resp = requests.post(API_URL, json=ex)
        if resp.status_code == 200:
            data = resp.json()
            print(f"Input: {ex['user_input']}")
            print(f"Prompt Version: {ex['prompt_version']}")
            print(f"Reply: {data['reply']}")
        else:
            print(f"Error: status code {resp.status_code}")
        print("-" * 50)

if __name__ == "__main__":
    test_api()