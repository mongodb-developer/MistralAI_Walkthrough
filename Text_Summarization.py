import requests

api_key = 'YOUR_API_KEY'
endpoint = 'https://api.mistral.ai/v1/generate'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

def summarize_text(text, max_tokens=150):
    prompt = f'Summarize the following text:\n\n{text}'
    payload = {
        'model': 'mixtral-8x7b',
        'prompt': prompt,
        'max_tokens': max_tokens
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        summary = response.json().get('text')
        return summary
    else:
        print(f'Error: {response.status_code}')
        print(response.json())
        return None

# Example usage
long_text = """
Artificial Intelligence (AI) has revolutionized the way we interact with technology. From voice assistants
to personalized recommendations, AI is embedded in our daily lives. The advancements in AI have enabled
machines to perform complex tasks with high accuracy, transforming industries such as healthcare,
finance, and transportation. The development of machine learning algorithms and deep neural networks
has been pivotal in this AI revolution. As AI continues to evolve, it is expected to bring even more
innovative solutions to global challenges.
"""
print("Summary:")
print(summarize_text(long_text))
