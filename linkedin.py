import requests
import base64
from config import key_linkedin
import json

# Your API endpoint

def get_data():
    url = f"https://api.company-information.service.gov.uk/company/{company_number}"

    # Your API key
    api_key = key_linkedin

    # Encode the API key to Base64 with a colon
    encoded_key = base64.b64encode(f'{api_key}:'.encode('utf-8')).decode('utf-8')

    # Set the Authorization header
    headers = {
        "Authorization": f"Basic {encoded_key}"
    }

    # Perform a GET request with the Authorization header
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Success
        data = response.json()
        # data = data['accounts']
        json_format = json.dumps(data, indent=2)
        print(json_format)
    else:
        # Handle the error
        print("Error:", response.status_code, response.text)
    
    return data