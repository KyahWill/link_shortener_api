import requests

url = 'https://www.youtube.com'
apiEndpoint = "http://localhost:5000/"
code = 'alias'
def get_link(url):
    response = requests.post(apiEndpoint,
        json={'url': url, 'code':code},
        headers={'Content-type': 'application/json'}
    )
    return response.content.decode()

def redirect(link):
    response = requests.get(apiEndpoint+link,)
    return response
# Print the response
link = get_link(url)
print(link)
# output = redirect(link) 

# print(output)
