import pandas as pd

df = pd.read_csv('Dataset .csv')

chain_counts = df['Restaurant Name'].value_counts()
chains = chain_counts[chain_counts > 1]

print(f"Total restaurant chains identified: {len(chains)}")
print("\nTop 10 Chains by Number of Outlets:")
print(chains.head(10))

chain_df = df[df['Restaurant Name'].isin(chains.index)]

chain_analysis = chain_df.groupby('Restaurant Name').agg(
    Total_Outlets=('Restaurant Name', 'count'),
    Average_Rating=('Aggregate rating', 'mean'),
    Total_Votes=('Votes', 'sum')
)

top_by_outlets = chain_analysis.sort_values(by='Total_Outlets', ascending=False).head(10)
print("\nTop 10 Chains by Outlets (with Rating and Popularity):")
print(top_by_outlets.round(2))

top_by_votes = chain_analysis.sort_values(by='Total_Votes', ascending=False).head(10)
print("\nTop 10 Most Popular Chains (by Total Votes):")
print(top_by_votes.round(2))

top_by_rating = chain_analysis[chain_analysis['Total_Outlets'] >= 5].sort_values(by='Average_Rating', ascending=False).head(10)
print("\nTop 10 Highest Rated Chains (Min 5 Outlets):")
print(top_by_rating.round(2))