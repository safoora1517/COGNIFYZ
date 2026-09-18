import pandas as pd

# Load dataset
df = pd.read_csv('Dataset .csv')


# 1. Determine percentage of restaurants with online delivery
delivery_counts = df['Has Online delivery'].value_counts()
delivery_percentages = (df['Has Online delivery'].value_counts(normalize=True)) * 100

print("=" * 55)
print("Online Delivery Distribution:")
for status, count in delivery_counts.items():
    print(f"  {status}: {count} ({delivery_percentages[status]:.2f}%)")

print(f"\nPercentage offering online delivery: {delivery_percentages.get('Yes', 0):.2f}%")


# 2. Compare average ratings (with vs without online delivery)
avg_rating_by_delivery = df.groupby('Has Online delivery')['Aggregate rating'].mean()

print("=" * 55)
print("Average Rating Comparison:")
print(f"  With Online Delivery (Yes):    {avg_rating_by_delivery.get('Yes', 0):.2f}")
print(f"  Without Online Delivery (No): {avg_rating_by_delivery.get('No', 0):.2f}")
print("=" * 55)