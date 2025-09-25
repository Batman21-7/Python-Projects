import requests
from bs4 import BeautifulSoup
import spotipy

CLIENT_ID = "4b99c63b9f414055bb63ef916c208b28"
CLIENT_SECRET = "d37871083b5b457fabdd11dd014a5313"

# Inputs Date
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

# Web Scraping Billboard Hot 100 for top 100 songs of given date
r = requests.get(url=URL)
webpage = r.text

soup = BeautifulSoup(webpage, 'html.parser')
songs = [song.getText().strip() for song in soup.select('div.o-chart-results-list-row-container li.lrv-u-width-100p '
                                                        'ul li h3')]
# print(songs)

# Spotify authorization using spotipy module as oauth2 is too complex

client = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        cache_path="token.txt",
        username="Batman217")
)

# Get user ID
user_id = client.current_user()['id']

# Get the URI for each song
tracks = []
for song in songs:
    try:
        tracks.append(client.search(q=f"track%3A{song}", type="track")['tracks']['items'][0]['external_urls']['spotify'])
    except IndexError:
        print(f"No song called {song}")

# Create new playlist and store the playlist ID received in response
playlistID = client.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)['id']

# Add all the songs to the playlist
client.user_playlist_add_tracks(user=user_id, playlist_id=playlistID, tracks=tracks)
