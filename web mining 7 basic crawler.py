import requests
from bs4 import BeautifulSoup

def web_crawler(url, keywords):
    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the text on the page
        page_text = soup.get_text()

        # Check if any of the keywords are present on the page
        for keyword in keywords:
            if keyword.lower() in page_text.lower():
                print(f'{keyword} found on {url}')
            else:
                print(f'{keyword} not found on {url}')

    else:
        print(f'Request failed with status code {response.status_code}')

# Example usage
url = input("Enter the URL to be searched")   #e.g.https://en.wikipedia.org/wiki/Web_crawler
keywords = []
print("Enter the keywords to be searched");
while(True):
    k=input("Enter the keyword")
    keywords.append(k)
    x=int(input("Enter 1 to give more keyword, enter 0 to exit"))
    if x==0:
        break
web_crawler(url, keywords)


