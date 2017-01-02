# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from confluence.settings import FACEBOOK_PAGE_ACCESS_TOKEN
import facebook


@shared_task(name='POST_TO_FACEBOOK')
#message=input("Please enter the message to be displayed: ")
def post_to_fb_page(message,link):
<<<<<<< HEAD
    graph = facebook.GraphAPI(access_token=FACEBOOK_PAGE_ACCESS_TOKEN)
=======
    graph = facebook.GraphAPI(access_token='EAAHZCnvXOZClgBAK7Llvam8SPZBPlrR8fffDmdeCBmmttUr09ZAep7NEOEh33ZC30UiQNEGUy5QZCDFi741TozPxMttZBtgmsnZAEzk364LU6co1BFN5vQbeAZBU262k7lz5CHbsMHVkAuFZC0HKSkbGB3GJgXdy5EX3giyZBUxAvR8MgZDZD')
>>>>>>> 70ba8b9c8ed6238c232795dc0e0c4c4973e9642c
    #message_entered=input("Please enter the message to be displayed: ")
    attachment =  {
    'link': link,   #must be same as picture
    'picture': link  #must be same as link
    }
    graph.put_wall_post(message=message, attachment=attachment)
<<<<<<< HEAD
    
=======
    return 'posted'
>>>>>>> 70ba8b9c8ed6238c232795dc0e0c4c4973e9642c
