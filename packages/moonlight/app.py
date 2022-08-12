import requests
from bs4 import BeautifulSoup
from lxml import html

# ccurrent placeholder
url = 'https://oxylabs.io/blog'
render_site = requests.get(url)
tree = html.fromstring(render_site.text)

# SOUPING to retutn a readable output
soup = BeautifulSoup(render_site.content, 'html.parser')
blog_titles = tree.xpath('//h2[@class="blog-card__content-title"]/text()')
for title in blog_titles:
    print(title)