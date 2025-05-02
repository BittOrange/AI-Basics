from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# read the data
superstore_data = pd.read_csv("superstore.csv", encoding="ISO-8859-1")

# calculate profit rate of all categories
superstore_data['profit_rate'] = superstore_data['Profit'] / superstore_data['Sales']
category_summary = superstore_data.groupby('Category')['profit_rate'].mean().sort_values(ascending=False)

# extract the top category
top_category = category_summary.index[0]
top_rate = round(category_summary.iloc[0]*100, 2)

# generate the prompt
prompt = f"""
We analyzed a sales dataset containing revenue and profit across different product categories.
The average profit rate (Profit/Sales) for each category is as follows:
{category_summary.to_string()}
Please provide a summary that includes:
1. Which product category has the highest average profit rate?
2. Why might this category have a higher profit rate? (Consider business logic and common sense)
3. One actionable recommendation to help improve overall profitability.

Please format your response in clear, structured paragraghs.
"""

# call the API
response = client.chat.completions.create(
    model = "gpt-4.1-mini",
    messages = [
        {"role": "system", "content": "You are a Senior Business Analyst"},
        {"role": "user", "content": prompt}
    ],
    response_format = {"type": "text"}
)

# print the response
print(response.choices[0].message.content)










