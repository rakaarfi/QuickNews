from requesting import get_requests

# Extract all links
def get_link(soup):
  # Find tag that have link inside
  article = soup.find('div', class_='grid-row list-content')

  # Find all links inside above tag
  links = article.find_all('h3', class_='media__title')

  # Iterate each link to an empty list
  link_list = []
  for link in links:
    link_tag = link.find('a', class_='media__link')
    href = link_tag.get('href')

    # Excluding some from link
    if len(href) > 50 and "https://20.detik.com/" not in href and "https://news.detik.com/foto-" not in href:
      link_list.append(href)
  
  print(f"Total link found: {len(link_list)}")
  return link_list

# Extract img URL, Title, Content, author, date
# Dont forget to add ?single=1 to each link below
def get_info(link):
  link = link + "?single=1"
  session = requests.Session()
  soup, status = get_requests(url=link, session=session)
  print(f"Getting image, title, content, author, date from {link}")

  info = {}
  if status == 200:
    # Find tag that have link inside
    article = soup.find('article', class_='detail')

    # Find title, author, date, img url
    try:
      img = article.find('img').get('src')
    except AttributeError as e:
      img = None
      print(f"An exception occurred in Image: {e}")

    title = validate_info(tag='h1', classes='detail__title', article=article).get_text(strip=True)
    author = validate_info(tag='div', classes='detail__author', article=article).get_text(strip=True)
    date = validate_info(tag='div', classes='detail__date', article=article).get_text(strip=True)    

    # Find content
    content = validate_info(tag='div', classes='detail__body-text itp_bodycontent', article=article)
    
    # Get first <strong> and all element <p>
    strong_element = content.find('strong')
    p_elements = content.find_all('p')

    # Exclude class='para_caption', "Simak Video", "Gambas" from element
    filtered_elements = [
        p for p in p_elements 
        if 'para_caption' not in p.get('class', []) and 
        "Simak Video" not in p.text and 
        "Gambas" not in p.text and 
        not p.find('a', href=True)
    ]
    list_element = []
    list_element.append(strong_element)
    for p in filtered_elements:
        list_element.append(p)

    info["Link"] = link
    info["Title"] = title
    info["Author"] = author
    info["Date"] = date
    info["Image URL"] = img
    info["Content"] = list_element

    print("Info added.")
  return info

def validate_info(tag, classes, article):
  try:
    info = article.find(tag, class_=classes)
  except AttributeError as e:
    info = None
    print(f"An exception occurred: {e}")
  return info

def get_info_all_links(links):
    all_info = []
    for index, link in enumerate(links):
        print(f"Processing link {index + 1} out of {len(links)}: {link}")
        info = get_info(link=link)
        if info:
            info["Index"] = index + 1  # Add index to info dict
            all_info.append(info)
  
    print("Completed getting all info from each link.")
    return all_info, index

# def get_info_all_links(links):
#   all_info = []
#   for link in links:
#     info = get_info(link=link)
#     all_info.append(info)
  
#   print ("Getting all info from each link")
#   return all_info

import requests
if __name__ == '__main__':
  # url = 'https://news.detik.com/indeks'
  # session = requests.Session()
  # soup, status = get_requests(url=url, session=session)
  # link = get_link(soup)
  get_info(link='https://news.detik.com/pilkada/d-7570174/didukung-1-000-nyai-cagub-luthfi-beberkan-program-pesantren-obah')