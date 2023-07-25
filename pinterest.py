import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_data(url):
    
    parsed_url = urlparse(url)
    if not parsed_url.netloc:
        url = "https://www.pinterest.com/" + parsed_url.path.strip('/')
    

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    pins = soup.find_all('div', {'data-test-id': 'pin'})

    data = []
    pint_url = 'https://www.pinterest.com'

    for i, pin in enumerate(pins):
        
        link = pin.find('a')['href']
        if not link.startswith('http'):
            link = urljoin(pint_url, link)

        
        link_response = requests.get(link)
        link_soup = BeautifulSoup(link_response.content, 'html.parser')

        data_loaded = link_soup.find(
            'script', {'data-test-id': 'leaf-snippet'})

        try:
            json_data = json.loads(data_loaded.string)

            image_url = json_data['image']
            print(image_url)
            
            headline = json_data['headline']

            pin_data = {
                'link': link,
                'image_url': image_url,
                'description': headline
            }
            data.append(pin_data)
            print('done')
        except:
            print('skipped')
            continue

    with open('pins.json', 'w') as file:
        json.dump(data, file, indent=4)

    print('Data saved to pins.json')


url = input()
extract_data(url)