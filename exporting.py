from datetime import datetime

# Main function to create the dictionary
def create_dict(resource, count, data):
    # Generate current time
    generated_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create the dictionary
    result = {
        "status code": 200,
        "message": "OK",
        "resource": resource,
        "count": count,
        "generated time": generated_time,
        "data": data
    }
    
    return result

from requesting import get_requests
from parsing import get_link
import requests

if __name__ == '__main__':
  url = 'https://news.detik.com/indeks'
  session = requests.Session()
  soup, status = get_requests(url, session=session)
  resource = get_resource()
  link = get_link(soup)

  output_dict = create_dict(resource, count=20)
  print(output_dict)