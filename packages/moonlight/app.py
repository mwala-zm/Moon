from bs4 import BeautifulSoup
import requests

def get_soup(URL):
    URL = ""
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup
