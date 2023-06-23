import requests
from bs4 import BeautifulSoup

#url = 'https://timesofindia.indiatimes.com/india;
url = 'https://timesofindia.indiatimes.com/india/maharashtra'
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('span', {'class': 'w_tle'})
    for headline in headlines:
        text = headline.text.strip()
        link = headline.find('a')['href']
        print("HeadLine: ",text)
        print("Link: https://timesofindia.indiatimes.com",link)
        print()
except Exception as e:
    print("Error:", e)
