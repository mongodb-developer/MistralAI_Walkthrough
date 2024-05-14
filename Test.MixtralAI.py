# Testing Mixtral AI in Python

This guide provides an example of how to use Mixtral AI's API to generate text. Ensure you have your API key ready.

## Prerequisites

1. Python 3.6 or later
2. `requests` library (install using `pip install requests`)

## Example Code

```python
import requests

# Replace 'YOUR_API_KEY' with your actual API key from Mixtral AI
api_key = 'YOUR_API_KEY'
endpoint = 'https://api.mistral.ai/v1/generate'

# Define the headers and payload for the API request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

payload = {
    'model': 'mixtral-8x7b',  # Specify the model you want to use
    'prompt': 'Explain the significance of Sparse Mixture-of-Experts in AI.',
    'max_tokens': 150  # Adjust the max tokens as needed
}

# Send the POST request to the Mixtral AI API
response = requests.post(endpoint, headers=headers, json=payload)

# Check the response status and print the generated text
if response.status_code == 200:
    generated_text = response.json().get('text')
    print('Generated Text:')
    print(generated_text)
else:
    print(f'Error: {response.status_code}')
    print(response.json())
