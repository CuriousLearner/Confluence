# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import facebook


@shared_task
#message=input("Please enter the message to be displayed: ")
def post_to_fb_page(message_entered,link):
    graph = facebook.GraphAPI(access_token='EAAHZCnvXOZClgBAK7Llvam8SPZBPlrR8fffDmdeCBmmttUr09ZAep7NEOEh33ZC30UiQNEGUy5QZCDFi741TozPxMttZBtgmsnZAEzk364LU6co1BFN5vQbeAZBU262k7lz5CHbsMHVkAuFZC0HKSkbGB3GJgXdy5EX3giyZBUxAvR8MgZDZD')
    #message_entered=input("Please enter the message to be displayed: ")
    attachment =  {
    #'name': name,
    'link': link,   #must be same as picture
    #'caption': caption,
    #'description': 'desc',
    'picture': link  #must be same as link
    }
    graph.put_wall_post(message=message_entered, attachment=attachment)
    return 'posted'
