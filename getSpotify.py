import pprint
import sys

import spotipy
import boto3
import base64
import spotipy.util as util
import simplejson as json
import requests
from spotipy.oauth2 import SpotifyClientCredentials

def getSpotifyTopTen(username):

    # Credentials setup
    # Loads in 'creds.json' values as a dictionary
    with open('spotify_creds.json') as f:
        credentials = json.loads(f.read())

    # Decrypts API keys and sets config values from the config file
    # Make sure this is loading KMS encrypted values in creds.json 
    # or else you may see a TypeError: Incorrect padding error
    client_id = decrypt(credentials["client_id"])
    client_secret = decrypt(credentials["client_secret"])
    refresh_token = decrypt(credentials["refresh_token"])    

    # Build the auth request for refreshing the otken
    auth_str = ("%s:%s" %(client_id, client_secret))
    auth_str = base64.urlsafe_b64encode(auth_str.encode())
    redirect_uri='http://localhost/'
    data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'redirect_uri': redirect_uri}
    headers = {'Authorization': 'Basic %s' %(auth_str)}

    p = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

    spotifyResponse = p.json()
    spotify_token = spotifyResponse['access_token']

    songs = []
    if spotify_token:
        sp = spotipy.Spotify(auth=spotify_token)
        sp.trace = False
        results = sp.current_user_top_tracks(time_range='short_term', limit=5)
        for i, item in enumerate(results['items']):
            toAdd = i+1, "//", item['name'], "//", item['artists'][0]['name'], "\n"
            songs += toAdd
        return(songs)
    else:
        return

def decrypt(ciphertext):
        """Decrypt ciphertext with KMS""" 
        kms = boto3.client('kms')
        print ('Decrypting ciphertext with KMS')
        plaintext = kms.decrypt(CiphertextBlob = base64.b64decode(ciphertext))['Plaintext']
        return plaintext