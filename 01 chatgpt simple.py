import openai

openai.api_key = "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"
msg = input("isi pesan\n")

completion  = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": msg}])

print(completion.choices[0]["message"]["content"])