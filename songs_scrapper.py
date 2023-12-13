from bs4 import BeautifulSoup
import lxml
import requests
from song_model import Song

BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/'


class SongScrapper:
    def __init__(self):
        self.songs = []

    def scrape_user_songs(self, date):
        url = BILLBOARD_URL + date

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        for item in soup.select('.o-chart-results-list-row #title-of-a-story'):
            song_name = item.getText().strip()
            artist_name = item.find_next_sibling('span').getText().strip()
            self.songs.append(Song(artist_name, song_name, date))
