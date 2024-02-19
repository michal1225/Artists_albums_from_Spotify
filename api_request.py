import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class ArtistsAlbumsAPI:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(client_id="482730f4d579405cbb60919eed874664",
                                                  client_secret="ce836b0761634292ae23e18afcfe28e3")
        )
        self.albums = []

    '''
    This function search artist_id for artist name
    '''

    def get_artist_id(self, artist_name):
        results = self.sp.search(q='artist:' + artist_name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist_id = items[0]['id']
            return artist_id
        else:
            print("Artist not found")
            return None

    '''
        This function search albums names and returns them in a list
    '''

    def get_artist_albums(self, artist_id):
        try:
            response = self.sp.artist_albums(artist_id=artist_id)
            items = response['items']
            for album in items:
                album_name = album['name']
                self.albums.append(album_name)
            return self.albums
        except:
            print("Something went wrong while retrieving")
            return None

    '''This function runs searching albums for defined artist'''

    def run_request(self, artist):
        return self.get_artist_albums(artist_id=self.get_artist_id(artist))
