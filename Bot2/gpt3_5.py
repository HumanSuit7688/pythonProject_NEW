import openai

openai.api_key = "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"
messages = []
role_gpt = input('Chat GPT info about himself: ')

while True:
    promt = input('Your promt: ')
    messages.append({"role": "assistant", 'content' : role_gpt})
    messages.append({"role": "user", 'content': promt})

    x = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    answer = x.choices[0].message.content
    print(f'ChatGPT: {answer}')
    messages.append({"role": "assistant", 'content': answer})

