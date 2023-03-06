import requests

# The API endpoint
postURL = "http://localhost:5000/"
# A GET request to the API
response = requests.post(postURL,
    json={'url':'https://www.youtube.com'},
    headers={'Content-type': 'application/json'}

)


# Print the response
response_json = response.content
print(response_json)
