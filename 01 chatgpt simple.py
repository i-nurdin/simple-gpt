import openai

openai.api_key = "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"

completion  = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": "Hello!"}])

print(completion.choices[0].message)