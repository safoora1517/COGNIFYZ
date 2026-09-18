import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Dataset .csv')

max_votes = df['Votes'].max()
min_votes = df['Votes'].min()

highest_voted = df[df['Votes'] == max_votes][['Restaurant Name', 'City', 'Votes', 'Aggregate rating']]
lowest_voted = df[df['Votes'] == min_votes][['Restaurant Name', 'City', 'Votes', 'Aggregate rating']]

print("=" * 65)
print(f"Restaurant(s) with the Highest Votes ({max_votes}):")
print(highest_voted.to_string(index=False))

print("\n" + "=" * 65)
print(f"Sample Restaurant(s) with the Lowest Votes ({min_votes}) [Total: {len(lowest_voted)}]:")
print(lowest_voted.head(5).to_string(index=False))

correlation = df['Votes'].corr(df['Aggregate rating'])
print("\n" + "=" * 65)
print(f"Correlation between Votes and Aggregate Rating: {correlation:.4f}")
print("=" * 65)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Votes', y='Aggregate rating', alpha=0.5, color='royalblue')
plt.title('Votes vs. Aggregate Rating', fontsize=13)
plt.xlabel('Number of Votes')
plt.ylabel('Aggregate Rating')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('votes_vs_rating.png')
plt.show()
