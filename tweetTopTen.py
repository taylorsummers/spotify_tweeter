import sparrow_kms
import getSpotify

def handler(event,context):
    tweet_list = getSpotify.getSpotifyTopTen('taylor7summers@gmail.com')
    """Sends random tweet from list of potential tweets"""
    sparrow_kms.send_tweet(tweet_list)