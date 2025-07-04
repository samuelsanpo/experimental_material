import matplotlib.pyplot as plt
import numpy as np

# This script generates charts comparing the performance of different tools on the HumanEval and MBPP datasets.
tools = ['Copilot (HumanEval)', 'ChatGPT (HumanEval)', 'Copilot (MBPP)', 'ChatGPT (MBPP)']
pass_at_1 = [0.4000, 0.6667, 0.7333, 0.6667]
test_case_accuracy = [0.7714, 0.9133, 0.8400, 0.8267]
syntax_validity = [0.9333, 1.0000, 1.0000, 1.0000]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# This chart compares the Pass@1 scores of different tools
plt.figure(figsize=(8, 5))
plt.bar(tools, pass_at_1, color=colors)
plt.ylim(0, 1)
plt.title("Pass@1 Comparison")
plt.ylabel("Score")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("pass_at_1_comparison.png")
plt.close()

# This chart compares the test case accuracy of different tools
plt.figure(figsize=(8, 5))
plt.bar(tools, test_case_accuracy, color=colors)
plt.ylim(0, 1)
plt.title("Test Case Accuracy Comparison")
plt.ylabel("Score")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("test_case_accuracy_comparison.png")
plt.close()

# This chart compares the syntax validity rates of different tools
plt.figure(figsize=(8, 5))
plt.bar(tools, syntax_validity, color=colors)
plt.ylim(0, 1)
plt.title("Syntax Validity Rate Comparison")
plt.ylabel("Score")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("syntax_validity_comparison.png")
plt.close()

