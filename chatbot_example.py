import requests

api_key = 'YOUR_API_KEY'
endpoint = 'https://api.mistral.ai/v1/generate'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

def chat_with_bot(user_input, max_tokens=150):
    prompt = f'You are a helpful AI assistant. Respond to the following input:\n\n{user_input}'
    payload = {
        'model': 'mixtral-8x7b',
        'prompt': prompt,
        'max_tokens': max_tokens
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        bot_response = response.json().get('text')
        return bot_response
    else:
        print(f'Error: {response.status_code}')
        print(response.json())
        return None

# Example usage
user_input = "What is the weather like today?"
print("Bot Response:")
print(chat_with_bot(user_input))
