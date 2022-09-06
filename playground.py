import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
from pprint import pprint

logger = logging.getLogger('examples.add_tracks_to_playlist')
logging.basicConfig(level='DEBUG')
scope = 'playlist-modify-public'




def main():
    ## this adds "Keep You Much Longer" - Akon to playlist 
    # tracks = ["spotify:track:1kiAXXEYooMvsFWyYaDhof"] # <- track id 
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    # sp.playlist_add_items("37i9dQZF1DX0AMssoUKCz7", tracks, 0)
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = 'plamere'

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace = True
    user = sp.user(username)
    pprint.pprint(user)
    
    


if __name__ == '__main__':
    main()

 # track id - '1kiAXXEYooMvsFWyYaDhof'