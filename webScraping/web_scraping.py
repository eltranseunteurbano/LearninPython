import requests
from bs4 import BeautifulSoup
import urllib

def run():
    for i in range(1,6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        img_container = soup.find(id='comic')

        img_url = img_container.find('img')['src']
        img_name = img_url.split('/')[-1]
        print('Descarganado "{}"'.format(img_name))
        urllib.request.urlretrieve('https:{}'.format(img_url), img_name)


if __name__ == '__main__':
    run()