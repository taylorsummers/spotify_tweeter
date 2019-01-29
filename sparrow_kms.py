#!/usr/bin/env python
import boto3
import base64
import random
import json
from twython import Twython

# Credentials setup
# Loads in 'creds.json' values as a dictionary
with open('creds.json') as f:
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
CONSUMER_KEY = decrypt(credentials["consumer_key"])
CONSUMER_SECRET = decrypt(credentials["consumer_secret"])
ACCESS_TOKEN_KEY = decrypt(credentials["access_token_key"])
ACCESS_TOKEN_SECRET = decrypt(credentials["access_token_secret"])

# Create the Twython Twitter client using our credentials
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                  ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)


def send_tweet(tweet_text):
    """Sends a tweet to Twitter"""
    twitter.update_status(status = tweet_text)



