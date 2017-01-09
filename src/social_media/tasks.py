# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from confluence.settings import FACEBOOK_PAGE_ACCESS_TOKEN
import facebook

@shared_task(name='social_media.tasks.post_to_facebook')
def post_to_facebook(message,link= None):
    graph = facebook.GraphAPI(access_token=FACEBOOK_PAGE_ACCESS_TOKEN)
    attachment =  {
        'link': link,   #must be same as picture
        'picture': link  #must be same as link
    }
    graph.put_wall_post(message=message, attachment=attachment)
