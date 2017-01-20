# Twitter tokens
from confluence.settings import TWITTER_CONSUMER_KEY
from confluence.settings import TWITTER_CONSUMER_SECRET
from confluence.settings import TWITTER_ACCESS_KEY
from confluence.settings import TWITTER_ACCESS_SECRET

import tweepy

twitter_auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY,
                                   TWITTER_CONSUMER_SECRET)
twitter_auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
twitter_api = tweepy.API(twitter_auth)
