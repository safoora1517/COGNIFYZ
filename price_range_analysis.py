import pandas as pd
import matplotlib.pyplot as plt

# Load dataset 
df = pd.read_csv('Dataset .csv')


# 1. Calculate percentage of restaurants in each price range
price_counts = df['Price range'].value_counts().sort_index()
price_percentages = (df['Price range'].value_counts(normalize=True).sort_index()) * 100

# Combine into a neat summary table
summary_df = pd.DataFrame({
    'Count': price_counts,
    'Percentage (%)': price_percentages.round(2)
})

print("=" * 45)
print("Price Range Distribution:")
print(summary_df)
print("=" * 45)


# 2. Create a bar chart to visualize the distribution
plt.figure(figsize=(8, 5))
bars = plt.bar(price_counts.index.astype(str), price_counts.values, color='teal', edgecolor='black', alpha=0.8)

# Add counts and percentages on top of each bar
for bar, pct in zip(bars, price_percentages):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 50, f'{yval}\n({pct:.1f}%)', 
             ha='center', va='bottom', fontsize=10)

plt.title('Distribution of Price Ranges Among Restaurants', fontsize=14, fontweight='bold')
plt.xlabel('Price Range', fontsize=12)
plt.ylabel('Number of Restaurants', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('price_range_distribution.png')
plt.show()