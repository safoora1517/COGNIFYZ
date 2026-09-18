import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Dataset .csv')

# 1. Analyze distribution of aggregate ratings & find most common range
bins = [0, 1, 2, 3, 4, 5]
labels = ['0.0 - 1.0', '1.1 - 2.0', '2.1 - 3.0', '3.1 - 4.0', '4.1 - 5.0']

# Categorize ratings into intervals
df['Rating Range'] = pd.cut(df['Aggregate rating'], bins=bins, labels=labels, include_lowest=True)

# Count restaurants in each range
rating_range_counts = df['Rating Range'].value_counts().sort_index()
most_common_range = rating_range_counts.idxmax()
most_common_count = rating_range_counts.max()

print("=" * 50)
print("Aggregate Rating Range Distribution:")
print(rating_range_counts)
print("-" * 50)
print(f"Most common rating range: {most_common_range} ({most_common_count} restaurants)")

# 2. Calculate the average number of votes received
average_votes = df['Votes'].mean()

print("=" * 50)
print(f"Average number of votes per restaurant: {average_votes:.2f}")
print("=" * 50)

# 3. Visualization: Histogram of Aggregate Ratings
plt.figure(figsize=(8, 5))
plt.hist(df['Aggregate rating'], bins=20, color='skyblue', edgecolor='black', alpha=0.8)

plt.title('Distribution of Aggregate Ratings', fontsize=14, fontweight='bold')
plt.xlabel('Aggregate Rating (0 - 5)', fontsize=12)
plt.ylabel('Number of Restaurants', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('rating_distribution.png')
plt.show()