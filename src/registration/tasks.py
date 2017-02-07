"""Contains celery tasks to migrate conference attendees from different
ticketing platforms."""

from __future__ import absolute_import, unicode_literals

from django.db.models import Max
from celery import shared_task

from .models import User
from .utils import call_explara_and_fetch_data, process_explara_data_and_populate_db
from .utils import call_meetup_and_fetch_data, process_meetup_data_and_populate_db

@shared_task(name='registration.tasks.sync_database_with_explara')
def sync_database_with_explara(EXPLARA_EVENT_ID):
    """Syncs all new conference attendees from explara with the
    application's database.

    Args:
      - EXPLARA_EVENT_ID: str. Event ID for the explara event.

    Returns:
      - None
    """

    # For having multiple paginated calls to Explara till all the data is
    # synced with the database
    while True:
        max_ticket_id = User.objects.all().aggregate(Max('ticket_id'))["ticket_id__max"]

        if not max_ticket_id:
            max_ticket_id = 0

        data = call_explara_and_fetch_data(EXPLARA_EVENT_ID, max_ticket_id)

        if data["status"] != 'success':
            print("Error from explara: ")
            print(data)
            break

        if not data["attendee"]:
            print("No attendees left now")
            break

        attendee_order_list = data['attendee']

        process_explara_data_and_populate_db(attendee_order_list)


@shared_task(name='registration.tasks.rsvp_from_meetup')
def get_rsvp_from_meetup(MEETUP_EVENT_ID):
    """
      Gets the rsvp list from meetup.com for a particular event.
    
    Reference meetup doc :
      - https://www.meetup.com/meetup_api/docs/2/rsvps/
    
    Args:
      - MEETUP_EVENT_ID : str. Event id of the group's event. 

    Returns:
      - None
    """

    # The event id is hardcoded for now. 
    # The api doc says events are paginated

    data = call_meetup_and_fetch_data(MEETUP_EVENT_ID)
    
    if data["status"] != "success":
        print("Could not fetch data from meetup")
        print(data)

    meetup_rsvp_list = data["results"]
    
    process_meetup_data_and_populate_db(meetup_rsvp_list)
