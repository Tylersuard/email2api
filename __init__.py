# email2api.py
import requests
import json

def parse_simple_string(simple_string):
    dict_result = {}
    items = simple_string.split(',')
    for item in items:
        key, value = item.split(':')
        dict_result[key.strip()] = value.strip()
    return dict_result

def email_to_url(email):
    parts = email.split('@')
    return f"https://www.{parts[1]}/{parts[0]}"

def try_different_api_key_labels(url, data, api_key, additional_headers):
    # List of possible API key labels
    api_key_labels = ["Authorization: Bearer", "API-Key", "Token"]

    for label in api_key_labels:
        headers = {label: api_key, 'Content-Type': 'application/json'}
        headers.update(additional_headers)

        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Attempt with header {label} failed: {e}")

    return None  # No successful attempts

def send(send_to, message, subject):
    parsed_subject = parse_simple_string(subject)
    api_key = parsed_subject.pop('api_key', None)  # Extract API key
    if not api_key:
        print("API key not provided in the subject.")
        return None

    data = parse_simple_string(message)
    url = email_to_url(send_to)

    return try_different_api_key_labels(url, data, api_key, parsed_subject)
