# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from confluence.settings import FACEBOOK_PAGE_ACCESS_TOKEN
import facebook


@shared_task(name='POST_TO_FACEBOOK')
#message=input("Please enter the message to be displayed: ")
def post_to_fb_page(message,link):
    graph = facebook.GraphAPI(access_token=FACEBOOK_PAGE_ACCESS_TOKEN)
    #message_entered=input("Please enter the message to be displayed: ")
    attachment =  {
    'link': link,   #must be same as picture
    'picture': link  #must be same as link
    }
    graph.put_wall_post(message=message, attachment=attachment)
    
