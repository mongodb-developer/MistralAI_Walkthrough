import requests

api_key = 'YOUR_API_KEY'
endpoint = 'https://api.mistral.ai/v1/generate'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

def translate_text(text, target_language, max_tokens=150):
    prompt = f'Translate the following text to {target_language}:\n\n{text}'
    payload = {
        'model': 'mixtral-8x7b',
        'prompt': prompt,
        'max_tokens': max_tokens
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        translation = response.json().get('text')
        return translation
    else:
        print(f'Error: {response.status_code}')
        print(response.json())
        return None

# Example usage
english_text = "Hello, how are you?"
print("Translation to French:")
print(translate_text(english_text, "French"))
