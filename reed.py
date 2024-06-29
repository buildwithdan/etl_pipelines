import requests
import base64
from config import key_reed
import json

# Your API endpoint
versionnumber = 2
keywords = 
locationName = 
employerId = 
distance = 

def get_data():
    url = f"https://www.reed.co.uk/api/{versionnumber}/search?keywords={keywords}&loc ationName={locationName}&employerId={employerId}&distanceFromLocation={distance in miles}"

    # Your API key
    api_key = key_reed

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