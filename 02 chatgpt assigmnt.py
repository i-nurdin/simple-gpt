import openai

openai.api_key  = "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"

messages = []
system_msg  = input("Silahkan masukkan perintah\n")
messages.append({"role":"system","content":system_msg})

print("udah ready nih!")
while input != "quit()":
    message = input()
    messages.append({"role":"user","content":message})
    respon  = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    reply   = respon["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})
    print("\n" + reply + "\n")