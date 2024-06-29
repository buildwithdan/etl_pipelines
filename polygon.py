from config import key_polygon
import json
import requests

ticker2 = "NVDA"
date2 = "2023-01-09"

def get_data_open_close(ticker, date):
    url = f"https://api.polygon.io/v1/open-close/{ticker}/{date}"

    # Your API key
    api_key = key_polygon

    # # Encode the API key to Base64 with a colon
    # encoded_key = base64.b64encode(f'{api_key}:'.encode('utf-8')).decode('utf-8')

    # Set the Authorization header
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Perform a GET request with the Authorization header
    response = requests.get(url, headers=headers)
    print(response)

    # Check the response status code
    if response.status_code == 200:
        # Success
        data = response.json()
        print(data)
        # data = data['accounts']
        json_format = json.dumps(data, indent=2)
        print(json_format)
    else:
        # Handle the error
        print("Error:", response.status_code, response.text)
    
    return data


get_data_open_close("NVDA","2024-01-01")
