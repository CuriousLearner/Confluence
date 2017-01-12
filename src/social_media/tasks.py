"""Contains celery tasks to post messages on various social media platforms."""
from __future__ import absolute_import, unicode_literals

# Import secret tokens from settings.
from confluence.settings import FACEBOOK_PAGE_ACCESS_TOKEN
from confluence.settings import TWITTER_PAGE_ACCESS_TOKEN
from celery import shared_task

# Import GraphAPI for posting attachment to facebook page.
from facebook import GraphAPI
from TwitterAPI import TwitterAPI

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)


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


@shared_task(name='social_media.tasks.post_to_twitter')
def post_to_twitter(status, path=None):
    """Posts a message to the Twitter page using TwitterAPI authenticated via
       `TWITTER_PAGE_ACCESS_TOKEN`.

       Args:
           - status: str. The content of the message to be posted on Twitter.
           - path: The path of the image from local system.

       Returns:
           - None

    """
    file = open(path, 'rb')
    data = file.read()
    api.request('statuses/update_with_media', {status: status}, {'media[]': data})
    print("posted")
