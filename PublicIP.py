import requests

def get_public_ip():
    try:
        # Send a request to the ipify API to get the public IP address
        response = requests.get('https://api.ipify.org?format=json')
        
        # If the request was successful, extract the IP from the response
        if response.status_code == 200:
            public_ip = response.json().get('ip')
            return public_ip
        else:
            return f"Failed to get IP: {response.status_code}"
    
    except requests.RequestException as e:
        return f"Error occurred: {e}"

# Uncomment the line below to test the function
print(get_public_ip())
