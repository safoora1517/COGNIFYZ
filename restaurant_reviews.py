import pandas as pd
from collections import Counter
import re

df = pd.read_csv('Dataset .csv')

# Use 'Rating text' if full text reviews are not present in the dataset
review_col = 'Rating text' if 'Rating text' in df.columns else 'Reviews'

reviews_df = df.dropna(subset=[review_col, 'Aggregate rating']).copy()

def clean_and_tokenize(text_series):
    words = []
    stop_words = {'the', 'a', 'an', 'and', 'or', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'is', 'it', 'not', 'rated'}
    for text in text_series.astype(str):
        tokens = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        words.extend([w for w in tokens if w not in stop_words])
    return Counter(words)

positive_reviews = reviews_df[reviews_df['Aggregate rating'] >= 4.0][review_col]
negative_reviews = reviews_df[reviews_df['Aggregate rating'] <= 2.5][review_col]

print("Top 10 Most Common Positive Keywords:")
print(pd.Series(clean_and_tokenize(positive_reviews).most_common(10)))

print("\nTop 10 Most Common Negative Keywords:")
print(pd.Series(clean_and_tokenize(negative_reviews).most_common(10)))

reviews_df['Review_Length_Chars'] = reviews_df[review_col].astype(str).apply(len)
reviews_df['Review_Length_Words'] = reviews_df[review_col].astype(str).apply(lambda x: len(x.split()))

print(f"\nAverage Review Length (Characters): {reviews_df['Review_Length_Chars'].mean():.2f}")
print(f"Average Review Length (Words): {reviews_df['Review_Length_Words'].mean():.2f}")

correlation_chars = reviews_df['Review_Length_Chars'].corr(reviews_df['Aggregate rating'])
correlation_words = reviews_df['Review_Length_Words'].corr(reviews_df['Aggregate rating'])

print(f"\nCorrelation between Review Length (Characters) and Rating: {correlation_chars:.4f}")
print(f"Correlation between Review Length (Words) and Rating: {correlation_words:.4f}")

avg_len_by_rating = reviews_df.groupby('Aggregate rating')['Review_Length_Words'].mean()
print("\nAverage Word Count by Rating (Sample):")
print(avg_len_by_rating.head(10).round(2))