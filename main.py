from songs_scrapper import SongScrapper
from spotify_manager import SpotifyManager

scrapper = SongScrapper()
spotify_manager = SpotifyManager()

selected_date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
scrapper.scrape_user_songs(selected_date)
spotify_manager.create_playlist(name=selected_date, songs=scrapper.songs)
