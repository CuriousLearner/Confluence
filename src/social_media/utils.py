# Twitter tokens
from confluence.settings import TWITTER_CONSUMER_KEY
from confluence.settings import TWITTER_CONSUMER_SECRET
from confluence.settings import TWITTER_ACCESS_KEY
from confluence.settings import TWITTER_ACCESS_SECRET

import tweepy


def twitter_api_authentication():
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
    return tweepy.API(auth)
