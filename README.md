# 🎬 Content Engagement Analyzer  
**Simulated Data Project — Amazon Prime Video / Advertising**

---

## Key Features & Benefits

*   **Engagement Rate Calculation:** Calculates the engagement rate for each content based on likes and views.
*   **Average Watch Time Analysis:** Determines the average watch time per view, providing insights into viewer retention.
*   **Top Content Identification:** Identifies and ranks top-performing content based on engagement metrics.
*   **Data-Driven Insights:** Provides data-driven insights to optimize content strategy and ad campaigns.

By completing this project, you will understand how to:  
- Translate audience data into actionable business insights  
- Identify top-performing content or ad creatives  
- Make data-driven recommendations for viewer engagement and marketing strategy  

---

## 🎯 Objectives
- Analyze engagement data for multiple Prime Video titles  
- Compute engagement rates and average watch time per view  
- Rank content performance and visualize insights  
- Recommend strategies for boosting viewer retention and ad effectiveness  

---
## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

*   **Python:** Version 3.6 or higher.
*   **pandas:** For data manipulation and analysis.  Install using: `pip install pandas`
*   **matplotlib:** For data visualization. Install using: `pip install matplotlib`
*   **Excel:** Microsoft Excel or a compatible application to open and read the `Content_data.xlsx` file.

## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/nusrat-rahman490/content_engagement_analyzer.git
    cd content_engagement_analyzer
    ```

2.  **Install dependencies:**

    ```bash
    pip install pandas matplotlib
    ```

3.  **Prepare your data:**

    *   Ensure you have an Excel file named `Content_data.xlsx` with relevant columns (e.g., `content_name`, `views`, `likes`, `watch_time_mins`).
    *   Place the `Content_data.xlsx` file in the same directory as `analyze_engagement.py`. The provided code uses the absolute path "/home/nusrat/Desktop/Spreadsheet/Content_data.xlsx" which you will need to update.

4.  **Update the file path:**

    *   Open `analyze_engagement.py` and modify the file path for loading the dataset to match the location of your `Content_data.xlsx` file. For example:

    ```python
    df = pd.read_excel("Content_data.xlsx") # if the data file is in the same directory
    # OR
    df = pd.read_excel("/path/to/your/Content_data.xlsx") # if the data file is in a different directory
    ```

## Usage Examples

To analyze the engagement data, run the `analyze_engagement.py` script:

```bash
python analyze_engagement.py
```

This will output a summary of the top 3 most engaging contents based on engagement rate. The script can be further customized to generate visualizations or perform more in-depth analysis.

Here's a snippet of the core analysis logic:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Content_data.xlsx")

# Calculate engagement metrics
df["engagement_rate"] = (df["likes"] / df["views"]) * 100
df["avg_watch_time_per_view"] = df["watch_time_mins"] / df["views"]

# Sort by engagement rate
top_content = df.sort_values(by="engagement_rate", ascending=False)

# Display summary
print("📊 Top 3 Engaging Contents:")
print(top_content[["content_name", "views", "likes", "engagement_rate", "avg_watch_time_per_view"]].head(3))

# Optional: Create a bar chart of engagement rates
plt.figure(figsize=(10, 6))
plt.bar(top_content["content_name"].head(10), top_content["engagement_rate"].head(10))
plt.xlabel("Content Name")
plt.ylabel("Engagement Rate (%)")
plt.title("Top 10 Content by Engagement Rate")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

## Configuration Options

*   **Data Source:** The primary configuration is the path to the `Content_data.xlsx` file. Ensure this path is correctly set in the `analyze_engagement.py` script.
*   **Analysis Metrics:** The script currently calculates engagement rate and average watch time per view. You can modify the script to calculate other metrics or analyze different aspects of the data.
*   **Visualization:** The script includes an optional visualization component that can be enabled or disabled as needed. You can further customize the visualization to display different data or use different chart types.

## Contributing Guidelines

Contributions are welcome! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, descriptive messages.
4.  Submit a pull request.

Please follow coding style conventions and include relevant tests with your contributions.

## License Information

This project has no specified license. All rights are reserved by the owner.

## Acknowledgments

*   pandas:  Powerful data analysis toolkit.
*   matplotlib:  Comprehensive library for creating static, animated, and interactive visualizations in Python.
