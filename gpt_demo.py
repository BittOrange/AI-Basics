from openai import OpenAI

client = OpenAI(api_key="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")

user_input = "帮我总结这段话：在当前快速变化的商业环境中，企业必须灵活调整战略，以应对市场的不确定性。"

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "你是一个擅长中文总结的助手。"},
        {"role": "user", "content": user_input}
    ]
)

print("模型回复：", response.choices[0].message.content)
