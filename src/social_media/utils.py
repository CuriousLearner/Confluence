from confluence.settings import TWITTER_CONSUMER_KEY
from confluence.settings import TWITTER_CONSUMER_SECRET

import tweepy

twitter_auth = tweepy.OAuthHandler(
                    TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET
                    )
