import requests
import concurrent.futures

# (Nama folder) + (.) + (nama file) import 
from NewsAggregator.requesting import get_requests
from NewsAggregator.parsing import get_link, get_info_all_links
from NewsAggregator.exporting import create_dict

def scraping_per_page(url, session):
  # Sends requests with a session.
  soup, status = get_requests(url, session)

  # Extract all links from the parsed HTML content using the 'get_link' function.
  link = get_link(soup)

  # Extract detailed information and its index from all link.
  # all_info, index = get_info_all_links(link)

  # Store all info to a dictionary.
  # result = create_dict(resource=url, count=index+1, data=link)

  return link

def scraping_multi_page(base_url):
  results = []
  #base_url = 'https://news.detik.com/indeks/'

  session = requests.Session()

  for i in range(1):
    url = f"{base_url+str(i)}"
    print(url)

    # Store all info to a dictionary.
    result = scraping_per_page(url, session=session)

    # Add the result in the empty list
    results.extend(result)

  # Extract detailed information and its index from all link.
  all_info, index = get_info_all_links(results)

  with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    executor.map(get_info_all_links, results)

  # Store all info to a dictionary.
  data = create_dict(resource=base_url, count=index+1, data=all_info)

  return data

if __name__ == '__main__':
  url = 'https://news.detik.com/indeks'
  result = scraping_multi_page(url)
  print(result)