import json
from pathlib import Path

PROMPT_DIR = Path("../prompts")
EVAL_SET = Path("eval_set.jsonl")

def load_prompts():
    return sorted(PROMPT_DIR.glob("*.json"))

def load_eval_set():
    with open(EVAL_SET, "r", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)

def mock_model(prompt, user_input):
    return f"[MOCK] {user_input}"

def run_eval():
    prompts = load_prompts()
    samples = list(load_eval_set())

    for prompt in prompts:
        print(f"\n=== Evaluating {prompt.name} ===")
        for sample in samples:
            output = mock_model(prompt, sample["input"])
            print(f"- Input: {sample['input']}")
            print(f"  Output: {output}")

if __name__ == "__main__":
    run_eval()