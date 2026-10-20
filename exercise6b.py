import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('scores.csv')
print(df.head())
print("\nMissing values:\n", df.isna().sum())

courses = ['math', 'python', 'database']          
colors  = {'math': 'tab:red', 'python': 'tab:blue', 'database': 'tab:green'}


plt.figure(figsize=(12, 6))
for c in courses:
    plt.scatter(df['student_id'], df[c], label=c, color=colors[c], s=45, alpha=0.85)
plt.xlabel('Student ID')
plt.ylabel('Marks')
plt.title('Student Scores: Math, Python, Database')
plt.xticks(rotation=90)
plt.legend(title='Course')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('scattered.png', dpi=150)
plt.close()


fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))
for ax, c in zip(axes, courses):
    ax.hist(df[c].dropna(), bins=8, color=colors[c], edgecolor='black')
    ax.set_title(f'{c} marks')
    ax.set_xlabel('Marks')
    ax.set_ylabel('Frequency')
plt.suptitle('Histogram of Marks per Course')
plt.tight_layout()
plt.savefig('histo.png', dpi=150)
plt.close()


plt.figure(figsize=(8, 6))
df.boxplot(column=courses, grid=False)     # one figure, 3 boxes side by side
plt.ylabel('Marks')
plt.title('Box Plot: Math, Python, Database')
plt.tight_layout()
plt.savefig('box.png', dpi=150)
plt.close()
