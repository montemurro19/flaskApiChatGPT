import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

def generateChatResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "You are a helpful assitant."})
    
    question = {}
    question['role'] = 'user'
    question['content'] = prompt

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages)

    try:
        answer = response['choices'][0]['message']['content']
    except:
        answer = 'oops! deu ruim.'

    return answer