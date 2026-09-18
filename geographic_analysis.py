import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Dataset .csv')

geo_df = df[(df['Longitude'] != 0) & (df['Latitude'] != 0)].dropna(subset=['Longitude', 'Latitude'])

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=geo_df, 
    x='Longitude', 
    y='Latitude', 
    hue='City', 
    legend=False, 
    alpha=0.6, 
    s=30
)

plt.title('Geographic Distribution of Restaurants')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('restaurant_locations.png')
plt.show()

city_clusters = geo_df['City'].value_counts()
print("Top 10 Restaurant Clusters by City:")
print(city_clusters.head(10))