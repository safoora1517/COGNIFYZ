import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset .csv')

# Percentage availability by price range
online_delivery_pct = (
    pd.crosstab(df['Price range'], df['Has Online delivery'], normalize='index') * 100
)
table_booking_pct = (
    pd.crosstab(df['Price range'], df['Has Table booking'], normalize='index') * 100
)

service_summary = pd.DataFrame({
    'Online Delivery (%)': online_delivery_pct.get('Yes', 0),
    'Table Booking (%)': table_booking_pct.get('Yes', 0)
}).round(2)

print("Percentage of Restaurants Offering Services by Price Range:")
print(service_summary)

# Plot grouped bar chart
service_summary.plot(kind='bar', figsize=(8, 5), edgecolor='black', alpha=0.85)
plt.title('Service Availability by Price Range', fontsize=13)
plt.xlabel('Price Range')
plt.ylabel('Percentage (%)')
plt.ylim(0, 100)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('services_vs_price_range.png')
plt.show()
