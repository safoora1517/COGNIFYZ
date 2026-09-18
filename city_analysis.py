import pandas as pd

# Load dataset
df = pd.read_csv('Dataset .csv')

# 1. Identify the city with the highest number of restaurants
city_counts = df['City'].value_counts()
top_restaurant_city = city_counts.idxmax()
top_restaurant_count = city_counts.max()

print("=" * 50)
print(f"City with highest number of restaurants: {top_restaurant_city} ({top_restaurant_count} restaurants)")


# 2. Calculate the average rating for restaurants in each city
avg_rating_per_city = df.groupby('City')['Aggregate rating'].mean()

print("=" * 50)
print("Average rating for restaurants in each city:")
print(avg_rating_per_city.round(2))

# 3. Determine the city with the highest average rating
top_rated_city = avg_rating_per_city.idxmax()
highest_avg_rating = avg_rating_per_city.max()

print("=" * 50)
print(f"City with the highest average rating: {top_rated_city} ({highest_avg_rating:.2f})")
print("=" * 50)