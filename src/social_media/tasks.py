'''This module is added to add various social media automated tasks.'''
from __future__ import absolute_import, unicode_literals

# Import secret tokens from settings.
from confluence.settings import FACEBOOK_PAGE_ACCESS_TOKEN
from celery import shared_task

# Import GraphAPI for posting attachment to facebook page.
from facebook import GraphAPI


# Create your tasks here
@shared_task(name='social_media.tasks.post_to_facebook')
def post_to_facebook(message, link=None):
    ''' The follwing task is designed to post a status to facebook page. It is
        taking message and link(optional) as parameters and post the message as
        status to facebook page and link as an attachment, if provided.
    '''
    graph = GraphAPI(access_token=FACEBOOK_PAGE_ACCESS_TOKEN)
    attachment = {
        'link': link,   # link to visit on clicking on the attachment.
        'picture': link  # link of the attachment to be posted.
    }
    graph.put_wall_post(message=message, attachment=attachment)
