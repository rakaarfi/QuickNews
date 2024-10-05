import requests

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
    if len(href) > 50 and "https://20.detik.com/" not in href and ".com/foto-" not in href:
      link_list.append(href)
  
  return link_list

# Extract img URL, Title, Content, author, date
def get_info(link):

  # Add ?single=1 to extract all pages from the news
  link = link + "?single=1"

  session = requests.Session()
  soup, status = get_requests(url=link, session=session)

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

    filtered = filtered_element(p_elements)

    list_element = []
    list_element.append(strong_element)
    for p in filtered:
        list_element.append(p)

    # Add info to the empty dictionary
    info["Link"] = link
    info["Title"] = title
    info["Author"] = author
    info["Date"] = date
    info["Image URL"] = img
    info["Content"] = list_element

  return info

def filtered_element(p_elements):
  # List of substrings to exclude
  exclude_substrings = ["Simak Video", "Gambas"]
  
  # Create a new list by filtering elements from p_elements
  filtered_elements = []
  
  # Loop through each paragraph
  for p in p_elements:
    # Check if the paragraph has the 'para_caption' class
    paragraph_classes = p.get('class', []) # If the paragraph doesn't have any class, it returns an empty list ([]).
    if 'para_caption' in paragraph_classes:
      continue  # Skip this paragraph

    # Check if the paragraph contains any of the excluded substrings
    for substring in exclude_substrings:
      if substring in p.text:
        continue  # Skip this paragraph if any excluded substring is found

    # Check if the paragraph contains a link (anchor tag with href)
    if p.find('a', href=True):
      continue  # Skip this paragraph

    filtered_elements.append(p)
  return filtered_elements

# Validating info
def validate_info(tag, classes, article):
  try:
    info = article.find(tag, class_=classes)
  except AttributeError as e:
    info = None
    print(f"An exception occurred: {e}")
  return info

# Extracting all info from all links
def get_info_all_links(links):
  all_info = []
  for index, link in enumerate(links):
    info = get_info(link=link)
    if info:
      info["Index"] = index + 1  # Add index to info dict
      all_info.append(info)

  return all_info, index