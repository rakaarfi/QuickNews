from requesting import get_requests
from parsing import get_link, get_info_all_links
from exporting import create_dict
import requests
from prettyprinter import pprint as pp

def main(url):
  session = requests.Session()
  soup, status = get_requests(url, session)
  link = get_link(soup)
  all_info, index = get_info_all_links(link)
  # exportPandas(all_info, 'testy')
  result = create_dict(resource=url, count=index, data=all_info)
  pp(result)
  return result

if __name__ == '__main__':
  url = 'https://news.detik.com/indeks'
  main(url)