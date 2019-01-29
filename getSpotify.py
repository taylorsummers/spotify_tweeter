import pprint
import sys

import spotipy
import boto3
import base64
import spotipy.util as util
import simplejson as json
from spotipy.oauth2 import SpotifyClientCredentials

def getSpotifyTopTen(username):

    # Credentials setup
    # Loads in 'creds.json' values as a dictionary
    with open('spotify_creds.json') as f:
        credentials = json.loads(f.read())

    def decrypt(ciphertext):
        """Decrypt ciphertext with KMS""" 
        kms = boto3.client('kms')
        print ('Decrypting ciphertext with KMS')
        plaintext = kms.decrypt(CiphertextBlob = base64.b64decode(ciphertext))['Plaintext']
        return plaintext

    # Decrypts API keys and sets config values from the config file
    # Make sure this is loading KMS encrypted values in creds.json 
    # or else you may see a TypeError: Incorrect padding error
    SPOTIPY_CLIENT_ID= decrypt(credentials["client_id"])
    SPOTIPY_CLIENT_SECRET = decrypt(credentials["client_secret"])

     # Request URLs for Spotify
    request_authorization_url = "https://accounts.spotify.com/authorize"
    request_token_url = "https://accounts.spotify.com/api/token"
    
    # the scope for the API requests
    scope = 'user-read-recently-played'

    scope = 'user-top-read'
    token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri='')
    songs = []
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.current_user_top_tracks(time_range='short_term', limit=5)
        for i, item in enumerate(results['items']):
            toAdd = i+1, "//", item['name'], "//", item['artists'][0]['name'], "\n"
            songs += toAdd
        return(songs)
            
    else:
        return