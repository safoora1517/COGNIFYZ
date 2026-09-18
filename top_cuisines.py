import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
file_path = "Dataset .csv"

if not os.path.exists(file_path):
    # Helps find the file if it's placed in the same folder as this script
    script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
    file_path = os.path.join(script_dir, "Dataset .csv")

df = pd.read_csv(file_path)

# 2. Drop rows where 'Cuisines' is missing
df_clean = df.dropna(subset=['Cuisines']).copy()
total_restaurants = len(df_clean)

# 3. Split multiple cuisines per restaurant and trim whitespace
cuisines_expanded = (
    df_clean['Cuisines']
    .str.split(',')
    .explode()
    .str.strip()
)

# 4. Identify top 3 cuisines
top_3_counts = cuisines_expanded.value_counts().head(3)

# 5. Compute percentage of restaurants serving each top cuisine
top_3_percentages = (top_3_counts / total_restaurants) * 100

# 6. Format output into a clean table
results_df = pd.DataFrame({
    'Cuisine': top_3_counts.index,
    'Restaurant Count': top_3_counts.values,
    'Percentage (%)': top_3_percentages.values.round(2)
})

print("=" * 45)
print("       LEVEL 1 - TASK 1: TOP CUISINES        ")
print("=" * 45)
print(results_df.to_string(index=False))
print("=" * 45)

# 7. Generate and display the plot
plt.figure(figsize=(7, 4.5))
ax = sns.barplot(
    data=results_df, 
    x='Cuisine', 
    y='Percentage (%)', 
    palette='viridis'
)

plt.title('Top 3 Cuisines Served by Percentage of Restaurants', fontsize=12, pad=12)
plt.xlabel('Cuisine', fontsize=10)
plt.ylabel('Percentage of Restaurants (%)', fontsize=10)
plt.ylim(0, results_df['Percentage (%)'].max() + 10)

# Add exact value labels on top of the bars
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.2f}%',
                (p.get_x() + p.get_width() / 2., height + 1),
                ha='center', va='bottom', fontsize=10, weight='bold')

plt.tight_layout()
plt.show()