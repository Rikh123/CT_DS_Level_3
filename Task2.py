#  Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Load the enhanced dataset
df = pd.read_csv("Enhanced_Dataset_Task3.csv")  # Ensure the file path is correct

#  Cuisine vs. Rating Analysis
# Split cuisines (assuming multiple cuisines are separated by commas)
df["Cuisines"] = df["Cuisines"].astype(str)  # Ensure data is in string format
df_expanded = df.assign(Cuisines=df["Cuisines"].str.split(", ")).explode("Cuisines")

# Compute average rating for each cuisine
cuisine_ratings = df_expanded.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False)

#   Identifying Most Popular Cuisines
cuisine_votes = df_expanded.groupby("Cuisines")["Votes"].sum().sort_values(ascending=False)

#  Visualization

#  Cuisine vs. Average Rating
plt.figure(figsize=(10, 5))
sns.barplot(y=cuisine_ratings.index[:10], x=cuisine_ratings.values[:10], hue=cuisine_ratings.index[:10], dodge=False, palette="viridis", legend=False)
plt.xlabel("Average Rating")
plt.ylabel("Cuisine Type")
plt.title("Top 10 Highest Rated Cuisines")
plt.show()

#  Most Popular Cuisines by Votes
plt.figure(figsize=(10, 5))
sns.barplot(y=cuisine_votes.index[:10], x=cuisine_votes.values[:10], hue=cuisine_votes.index[:10], dodge=False, palette="coolwarm", legend=False)
plt.xlabel("Total Votes")
plt.ylabel("Cuisine Type")
plt.title("Top 10 Most Popular Cuisines by Votes")
plt.show()

#  Save results
cuisine_ratings.to_csv("Cuisine_Average_Ratings.csv")
cuisine_votes.to_csv("Cuisine_Popularity.csv")

#  Customer Preference Analysis Completed!
print("\n📊 Customer Preference Analysis Completed! Results saved as 'Cuisine_Average_Ratings.csv' and 'Cuisine_Popularity.csv'.")
