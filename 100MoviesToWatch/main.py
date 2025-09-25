import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

r = requests.get(url=URL)
webpage = r.text

soup = BeautifulSoup(webpage, 'html.parser')

titles = [title.getText() for title in soup.find_all(name='h3', class_='title')]
titles.reverse()
arr = ''
for title in titles:
    arr += (title + '\n')
print(arr)

with open('movies.txt', 'w', encoding='utf-8') as file:
    file.write(arr)
