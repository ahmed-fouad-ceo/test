import requests

def fetch_url(url):
    response = requests.get(url)
    return response.content

if __name__ == "__main__":
    url = input("Enter a URL: ")
    content = fetch_url(url)
    print(content)
