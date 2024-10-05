import requests
from prettyprinter import pprint as pp

from requesting import get_requests
from parsing import get_link, get_info_all_links
from exporting import create_dict

def main(url):
  # Create a session for making HTTP requests.
  session = requests.Session()

  # Sends requests with a session.
  soup, status = get_requests(url, session)

  # Extract all links from the parsed HTML content using the 'get_link' function.
  link = get_link(soup)

  # Extract detailed information and its index from all link.
  all_info, index = get_info_all_links(link)

  # Store all info to a dictionary.
  result = create_dict(resource=url, count=index+1, data=all_info)

  return result

if __name__ == '__main__':
  url = 'https://news.detik.com/indeks'
  result = main(url)