import requests

# URL of the webpage you want to fetch
url = 'https://example.com'

# Send a GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the content of the webpage
    print(response.text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
