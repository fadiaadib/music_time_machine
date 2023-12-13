class Song:
    def __init__(self, artist, name, date: str):
        self.artist = artist
        self.name = name
        self.year = date.split('-')[0]

    def __str__(self):
        return f'Artist: {self.artist} - Song: {self.name} - Year: {self.year}\n'
