
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import sys
from pprint import pprint
import time
import json

scopes = 'user-read-recently-played playlist-modify-public playlist-modify-private playlist-read-private'
user_id = "davidmchoi19"

def pull_song_ids(playlist_id):
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        p_items = sp.playlist_items(playlist_id)
        ids = []

        for item in p_items["items"]:
            ids.append(item["track"]['id'])
        
        return ids

class Spotify:
    def get_playlists(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))
        playlists = sp.user_playlists('davidmchoi19', limit = 50, offset = 0)
        return playlists 

    def get_recently_played(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))
        recently_played = sp.current_user_recently_played(limit=50, after=None, before=None)

        song_ids = []
        for item in recently_played['items']:
            song_ids.append(item['track']['id'])
            
        return song_ids

    def add_tracks(self, playlist_id, items):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))
        songs_in_list = pull_song_ids(playlist_id)
        songs_not_in = []

        for item in items:
            if item not in songs_in_list:
                songs_not_in.append(item)
        
        listy = json.dumps(songs_not_in)
        pprint(songs_not_in, indent=4)
        pprint(items, indent=4)

        sp.playlist_add_items(playlist_id, listy, 0)


    def pull_songs(self, songs):
        seen = set()
        dupes = []
        for x in songs:
            if x in seen and x not in dupes:
                dupes.append(x)
            else:
                seen.add(x)
        return dupes
        

# create new Spotify object, retrieve user playlists
a = Spotify()
playlists = a.get_playlists()


for i, item in enumerate(playlists['items']):
            print("%d. %s" % (i, item['name']))
valid = True

print('Select playlist to use: ')
while valid:
    num_input = input()
    if num_input.isnumeric() == False:
        print("Invalid. Enter a number: ")
    elif int(num_input) > len(playlists['items']) - 1:
        print('Select a number within the range: ')
    else:
        if playlists['items'][int(num_input)]['owner']['id'] != user_id:
            print("You cannot modify this playlist. Select a playlist you created: ")
        else:
            valid = False 

sel_playlist = playlists['items'][int(num_input)]
playlist_id = sel_playlist['id']
played = a.get_recently_played()

continue_prog = True

# pprint(
#     sel_playlist,
#     indent=4
# )


while(continue_prog):
    songs_to_add = a.pull_songs(played)
    a.add_tracks(playlist_id, songs_to_add)
    print("Playlist updated! Press 0 to terminate program: ")
    time.sleep(9850)

print('Program terminated!')




