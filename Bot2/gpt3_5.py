import openai

openai.api_key = "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"

while True:
    promt = input()
    messages = [{"role": "user", "content": promt}]

    x = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    answer = x.choices[0].message.content
    messages.append({"role": "system", 'content': answer})

    print(answer)
