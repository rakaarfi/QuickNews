import requests
from bs4 import BeautifulSoup as bs

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_requests(url, session:requests.Session):
  response = session.get(url, headers=headers)
  if response.status_code == 200:
      soup = bs(response.content, 'html.parser')
      return soup, response.status_code
  else:
      soup = None
      print(f"Failed to get response from {url}, status code: {response.status_code}")
  return soup, response.status_code

if __name__ == "__main__":
    url = 'https://news.detik.com/indeks'
    session = requests.Session()
    soup, status = get_requests(url=url, session=session)
    url = get_resource()
    if soup:
        print(soup)
    else:
        print(f"Failed to load page, status code: {status}")