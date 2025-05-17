import os, json, requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# JDoodle API credentials (load "client_id" and "client_secret" from .env file)
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

# Pascal code to execute
pascal_code = """
program HelloWorld;
begin
  writeln('Hello, World!');
end.
"""

# JDoodle API endpoint
url = 'https://api.jdoodle.com/v1/execute'

# Set the payload
payload = {
    'clientId': client_id,
    'clientSecret': client_secret,
    'script': pascal_code,
    'stdin': '',
    'language': 'pascal',
    'versionIndex': '0'
}

# Convert the payload to JSON
payload = json.dumps(payload)

# Set the headers
headers = {
    'Content-Type': 'application/json'
}

# Send the POST request
response = requests.post(url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    # Get the output from the response
    output = response.json()['output']

    # Print the output
    print(output)
else:
    print('Failed to execute Pascal code.')
    print('Status code:', response.status_code)