class Song:
    #We will use this attribute to keep track of the number of new songs that are created from the Song class
    count=0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}
    all_songs=[]
    all_artists=[]
    def __init__(self,name,artist,genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        Song.add_to_song_count()
        Song.add_to_song_genres(genre)
        Song.add_to_song_artists(artist)
        Song.all_songs.append(self) 
        Song.all_artists.append(self)
        Song.add_to_genre_count()
        Song.add_to_artist_count()
        

    @classmethod
    def add_to_song_count(cls,increment=1):
        cls.count+=increment

    @classmethod
    def add_to_song_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)


    @classmethod
    def add_to_song_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {genre: 0 for genre in cls.genres}  # Reset the genre count dictionary
        for song in cls.all_songs:
                cls.genre_count[song.genre] += 1

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {artist: 0 for artist in cls.artists}  
        for a in cls.all_artists:
            print("Artist:", a)
            cls.artist_count[a.artist] += 1
            print("Artist Count:", cls.artist_count)
         


klm=Song("kl","Ushre and Klm","rap")
klm.add_to_artist_count()
