import matplotlib.pyplot as plt
import numpy as np

# Error counts by category for each tool and benchmark
categories = ['Logic Errors', 'Incomplete Impl.', 'Incorrect Cond.', 'Missing Edge Cases']
tools = ['Copilot (HumanEval)', 'ChatGPT (HumanEval)', 'Copilot (MBPP)', 'ChatGPT (MBPP)']

data = np.array([
    [3, 2, 2, 2],  # Copilot (HumanEval)
    [3, 0, 1, 1],  # ChatGPT (HumanEval)
    [1, 1, 1, 1],  # Copilot (MBPP)
    [2, 1, 1, 1],  # ChatGPT (MBPP)
])

# Plot grouped bar chart
x = np.arange(len(tools))
bar_width = 0.2

fig, ax = plt.subplots(figsize=(10, 6))
for i in range(len(categories)):
    ax.bar(x + i * bar_width, data[:, i], bar_width, label=categories[i])

ax.set_xlabel('Tool and Benchmark')
ax.set_ylabel('Error Count')
ax.set_title('Distribution of Qualitative Error Types')
ax.set_xticks(x + bar_width * 1.5)
ax.set_xticklabels(tools, rotation=45, ha='right')
ax.legend()
plt.tight_layout()
plt.savefig('qualitative_errors_bar.png')
plt.close()

# Generate overall error distribution pie chart
total_by_category = data.sum(axis=0)
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
plt.figure(figsize=(6, 6))
plt.pie(total_by_category, labels=categories, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Overall Distribution of Qualitative Error Types')
plt.tight_layout()
plt.savefig('qualitative_errors_pie.png')
plt.close()
