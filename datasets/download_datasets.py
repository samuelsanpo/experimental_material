from datasets import load_dataset
import json

# Download and process HumanEval
print("Downloading HumanEval...")
humaneval = load_dataset("openai_humaneval", split="test")

humaneval_output = {}
for i, example in enumerate(humaneval):
    problem_id = f"humaneval_{i+1:03d}"
    humaneval_output[problem_id] = {
        "task_id": example["task_id"],
        "prompt": example["prompt"],
        "entry_point": example["entry_point"],
        "canonical_solution": example["canonical_solution"],
        "test": example["test"]
    }

print(f"✅ HumanEval: {len(humaneval_output)} problems processed.")

# Save HumanEval to JSON
with open("humaneval_dataset.json", "w", encoding="utf-8") as f:
    json.dump(humaneval_output, f, indent=2)

print("✅ Saved as 'humaneval_dataset.json'")

# Download and process MBPP 
print("Downloading MBPP...")
mbpp = load_dataset("mbpp", split="test")

mbpp_output = {}
for i, example in enumerate(mbpp):
    problem_id = f"mbpp_{i+1:03d}"
    mbpp_output[problem_id] = {
        "text": example["text"],
        "code": example["code"],
        "test_list": example["test_list"]
    }

print(f"✅ MBPP: {len(mbpp_output)} problems processed.")

# Save MBPP to JSON
with open("mbpp_dataset.json", "w", encoding="utf-8") as f:
    json.dump(mbpp_output, f, indent=2)

print("✅ Saved as 'mbpp_dataset.json'")
