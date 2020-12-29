from bs4 import BeautifulSoup
import requests
from .models import Project

contentLink = str(Project.getLink())

content = requests.get(contentLink).text

soup = BeautifulSoup(content, 'lxml')

about = soup.find('p', class_='f4 mt-3').text


print(about)
