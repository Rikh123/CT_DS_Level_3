#  Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Load the dataset
df = pd.read_csv("Enhanced_Dataset_Task3.csv")  # Ensure the file path is correct

# Distribution of Ratings (Histogram)
plt.figure(figsize=(8, 5))
sns.histplot(df["Aggregate rating"], bins=10, kde=True, color="blue")
plt.xlabel("Aggregate Rating")
plt.ylabel("Count")
plt.title("Distribution of Ratings")
plt.show()

# Average Ratings by Cuisine
df["Cuisines"] = df["Cuisines"].astype(str)
df_expanded = df.assign(Cuisines=df["Cuisines"].str.split(", ")).explode("Cuisines")
cuisine_avg_rating = df_expanded.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False)[:10]

plt.figure(figsize=(10, 5))
sns.barplot(y=cuisine_avg_rating.index, x=cuisine_avg_rating.values, hue=cuisine_avg_rating.index, palette="magma", legend=False)
plt.xlabel("Average Rating")
plt.ylabel("Cuisine")
plt.title("Top 10 Cuisines with Highest Ratings")
plt.show()

#  Average Ratings by City
city_avg_rating = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False)[:10]

plt.figure(figsize=(10, 5))
sns.barplot(y=city_avg_rating.index, x=city_avg_rating.values, hue=city_avg_rating.index, palette="coolwarm", legend=False)
plt.xlabel("Average Rating")
plt.ylabel("City")
plt.title("Top 10 Cities with Highest Restaurant Ratings")
plt.show()

#  Relationship Between Price Range & Rating
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Price range"], y=df["Aggregate rating"], hue=df["Price range"], palette="Set2", legend=False)
plt.xlabel("Price Range")
plt.ylabel("Aggregate Rating")
plt.title("Price Range vs. Rating")
plt.show()

#  Votes vs. Ratings Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Votes"], y=df["Aggregate rating"], alpha=0.6, color="purple")
plt.xlabel("Number of Votes")
plt.ylabel("Aggregate Rating")
plt.title("Votes vs. Aggregate Rating")
plt.show()

#  Save results
cuisine_avg_rating.to_csv("Cuisine_Average_Ratings_Visualization.csv")
city_avg_rating.to_csv("City_Average_Ratings_Visualization.csv")

#  Data Visualization Completed!
print("\n📊 Data Visualization Completed! Results saved as 'Cuisine_Average_Ratings_Visualization.csv' and 'City_Average_Ratings_Visualization.csv'.")
