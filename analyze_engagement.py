import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("/home/nusrat/Desktop/Spreadsheet/Content_data.xlsx")

# Calculate engagement metrics
df["engagement_rate"] = (df["likes"] / df["views"]) * 100
df["avg_watch_time_per_view"] = df["watch_time_mins"] / df["views"]

# Sort by engagement rate
top_content = df.sort_values(by="engagement_rate", ascending=False)

# Display summary
print("📊 Top 3 Engaging Contents:")
print(top_content[["content_name", "views", "likes", "engagement_rate"]].head(3))

print("\nAverage Watch Time per View (mins):")
print(df[["content_name", "avg_watch_time_per_view"]])

# Plot engagement rate chart
plt.figure(figsize=(8, 5))
plt.bar(df["content_name"], df["engagement_rate"])
plt.title("Content Engagement Rate (%)")
plt.ylabel("Engagement Rate (%)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
