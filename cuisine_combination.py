import pandas as pd

# Load dataset
df = pd.read_csv('Dataset .csv')

# Drop rows with missing values in 'Cuisines' or 'Aggregate rating'
df_cleaned = df.dropna(subset=['Cuisines', 'Aggregate rating']).copy()

# 1. Identify the most common combinations of cuisines
cuisine_counts = df_cleaned['Cuisines'].value_counts()

print("=" * 60)
print("Top 10 Most Common Cuisine Combinations:")
print("=" * 60)
print(cuisine_counts.head(10).to_string())

# 2. Determine if certain cuisine combinations have higher ratings
cuisine_ratings = df_cleaned.groupby('Cuisines')['Aggregate rating'].agg(
    Average_Rating='mean',
    Restaurant_Count='count'
)

# Sort strictly by highest average rating
top_rated_combinations = cuisine_ratings.sort_values(by='Average_Rating', ascending=False)

print("\n" + "=" * 60)
print("Top 10 Cuisine Combinations with the Highest Average Ratings:")
print("=" * 60)
print(top_rated_combinations.head(10).round(2).to_string())

frequent_combinations = cuisine_ratings[cuisine_ratings['Restaurant_Count'] >= 10]
top_rated_frequent = frequent_combinations.sort_values(by='Average_Rating', ascending=False)

print("\n" + "=" * 60)
print("Top 10 Highest Rated Combinations (Among Frequent: >= 10 restaurants):")
print("=" * 60)
print(top_rated_frequent.head(10).round(2).to_string())