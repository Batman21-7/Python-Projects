from bs4 import BeautifulSoup
import requests

r = requests.get(url="https://news.ycombinator.com/")

yc_webpage = r.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

spans = soup.find_all(name='span', class_='titleline')
titles = [title.a.getText() for title in spans]
links = [title.a.get('href') for title in spans]

scores = [int(score.getText().split(' ')[0]) for score in soup.find_all(name='span', class_='score')]

max_index = scores.index(max(scores))

print(f"Title: {titles[max_index]},\n Link: {links[max_index]},\n Score: {scores[max_index]}")
