# Create your tasks here
from __future__ import absolute_import, unicode_literals
from .celery import app

#import facebook

@app.task
def put_wall_post():
    graph = facebook.GraphAPI(access_token='page_token')

    attachment =  {
        'name': 'Link name',
        'link': 'https://conference.pydelhi.org/img/logo.png',   #must be same as picture
        'caption': 'Testing code',
        'description': 'PIC',
        'picture': 'https://conference.pydelhi.org/img/logo.png'  #must be same as link
    }
    graph.put_wall_post(message='Check this out...', attachment=attachment)
