"""Contains celery tasks to post messages on various social media platforms."""
from __future__ import absolute_import, unicode_literals

# Import secret tokens from settings.
from confluence.settings import FACEBOOK_PAGE_ACCESS_TOKEN
from confluence.settings import TWITTER_CONSUMER_KEY
from confluence.settings import TWITTER_CONSUMER_SECRET
from confluence.settings import TWITTER_ACCESS_KEY
from confluence.settings import TWITTER_ACCESS_SECRET

# Import shared tasks
from celery import shared_task

# Import GraphAPI for posting attachment to facebook page.
from facebook import GraphAPI
# Import tweepy and requests for twitter posts.
import os
import tweepy
import requests

# Create your tasks here


@shared_task(name='social_media.tasks.post_to_facebook')
def post_to_facebook(message, link=None):
    """Posts a message to the Facebook page using GraphAPI authenticated via
       `FACEBOOK_PAGE_ACCESS_TOKEN`.

       Args:
           - message: str. The content of the message to be posted on Facebook.
           - link: str. (Optional) Url of the attachment to be posted along
             with message.

       Returns:
           - None

    """
    graph = GraphAPI(access_token=FACEBOOK_PAGE_ACCESS_TOKEN)
    attachment = {
        'link': link,   # link to visit on clicking on the attachment.
        'picture': link  # link of the attachment to be posted.
    }
    graph.put_wall_post(message=message, attachment=attachment)


@shared_task(name='social_media.tasks.tweeet_to_twitter')
def tweet_to_twitter(message, url=None):
    """Posts a message to the Twitter page using TwitterAPI authenticated via
       TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY and
       TWITTER_ACCESS_SECRET.

       Args:
           - message: str. The content of the message to be posted on Twitter.
           - link: (Optional) Url of the attachment to be posted along
             with message.

       Returns:
           - None

    """
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)

    if url is not None:
        filename = 'image.jpg'
        request = requests.get(url, stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)
            api.update_with_media(filename, status=message)
            os.remove(filename)
        else:
            print("Unable to download image")
    else:
        api.update_status(message)
