import os
import openai

# 需要输入一个openai官方提供的key秘钥
# 可以自行去官网生成这key

openai.api_key = "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"


def chatGPT(start_sequence: str) -> str:
    prompt = start_sequence
    try:
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = prompt,
            temperature = 1,
            # 回答的文字长度
            max_tokens = 2000,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        return str(e)

def chat(prompt):  #定义一个函数，以便后面反复调用
    try:
        response = openai.Completion.create(
                  model="text-davinci-003",
                  prompt= prompt,
                  temperature=0.9,
                  max_tokens=2500,
                  top_p=1,
                  frequency_penalty=0.0,
                  presence_penalty=0.6
                  #stop=[" Human:", " AI:"]
                )
        return  response["choices"][0]["text"].strip()
    except Exception as exc:
        #print(exc)  #如果需要打印出故障原因可以使用本行代码，如果想增强美感，就屏蔽它。
        return "broken"

def chatGPT35(start_sequence: str) -> str:
    messages = start_sequence
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
            # 回答的文字长度
            max_tokens=4000,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.get("choices")[0]["message"]["content"]

    except Exception as e:
        return str(e)