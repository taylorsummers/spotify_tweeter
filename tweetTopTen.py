import sparrow_kms
import getSpotify

def handler(event,context):
    tweet_list = getSpotify.getSpotifyTopTen('taylor7summers@gmail.com')
    print(tweet_list)
    # Tweets out the list of songs
    sparrow_kms.send_tweet(tweet_list)