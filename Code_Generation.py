import requests

api_key = 'YOUR_API_KEY'
endpoint = 'https://api.mistral.ai/v1/generate'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

def generate_code(description, max_tokens=200):
    prompt = f'Generate a Python code snippet that performs the following task:\n\n{description}'
    payload = {
        'model': 'mixtral-8x7b',
        'prompt': prompt,
        'max_tokens': max_tokens
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        code_snippet = response.json().get('text')
        return code_snippet
    else:
        print(f'Error: {response.status_code}')
        print(response.json())
        return None

# Example usage
task_description = "Read a CSV file and print the first five rows."
print("Generated Code:")
print(generate_code(task_description))
