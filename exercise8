import pandas as pd
import matplotlib.pyplot as plt
import pickle



df = pd.read_csv('scores.csv')

courses = ['math', 'python', 'database']


plt.figure(figsize=(12, 6))
plt.scatter(df['student_id'], df['math'], label='Math', color='red', alpha=0.7)
plt.scatter(df['student_id'], df['python'], label='Python', color='blue', alpha=0.7)
plt.scatter(df['student_id'], df['database'], label='Database', color='green', alpha=0.7)

plt.xlabel('Student ID')
plt.ylabel('Scores')
plt.title('Student Scores (Math, Python, DB)')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig('scattered.png')
plt.close()


fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Math histogram
axes[0].hist(df['math'].dropna(), bins=10, color='red', edgecolor='black')
axes[0].set_title('Math Marks')
axes[0].set_xlabel('Marks')
axes[0].set_ylabel('Frequency')

# Python histogram
axes[1].hist(df['python'].dropna(), bins=10, color='blue', edgecolor='black')
axes[1].set_title('Python Marks')
axes[1].set_xlabel('Marks')
axes[1].set_ylabel('Frequency')

# Database histogram
axes[2].hist(df['database'].dropna(), bins=10, color='green', edgecolor='black')
axes[2].set_title('Database Marks')
axes[2].set_xlabel('Marks')
axes[2].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('histo.png')
plt.close()


plt.figure(figsize=(8, 6))
df.boxplot(column=courses, grid=False)
plt.title('Box Plot: Math, Python, DB')
plt.ylabel('Marks')
plt.tight_layout()
plt.savefig('box.png')
plt.close()


state = {
    'dataframe': df,
    'means': df[courses].mean().to_dict()
}

with open('state.pkl', 'wb') as f:
    pickle.dump(state, f)

print("Plots saved: scattered.png, histo.png, box.png")
print("Data pickled to: state.pkl")

# --- Optional: Verify the pickle works by loading it back ---
with open('state.pkl', 'rb') as f:
    loaded_state = pickle.load(f)
    print("Loaded pickled means:", loaded_state['means'])
