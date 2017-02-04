import requests

from confluence.settings import EXPLARA_API_KEY, EXPLARA_ATTENDEE_LIST_URL
from .models import User


def call_explara_and_fetch_data(EXPLARA_EVENT_ID, max_ticket_id):
    """Syncs all new conference attendees from Explara with the
    application's database.

    Args:
      - EXPLARA_EVENT_ID: str. Event ID for the Explara event.
      - max_ticket_id: int. ticket_id till which Explara data is already
            synced with the db.

    Returns:
      - Attendees data: dict. Response in JSON format as fetched from Explara.
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': "Bearer %s" % EXPLARA_API_KEY
    }

    payload = {
        'eventId': EXPLARA_EVENT_ID,
        'fromRecord': int(max_ticket_id),
        'toRecord': int(max_ticket_id) + 50
    }

    response = requests.post(
        EXPLARA_ATTENDEE_LIST_URL,
        data=payload,
        headers=headers
    )

    return response.json()


def process_explara_data_and_populate_db(attendee_order_list):
    """Syncs all new conference attendees from explara with the
    application's database.

    Args:
      - attendee_order_list: list. Attendees list as fetched from Explara's API.

    Returns:
      - None.
    """
    for order in attendee_order_list:
        tickets = order['attendee']
        for ticket in tickets:
            print(ticket)
            try:
                name, email = ticket['name'], ticket['email']
                ticket_no = ticket['ticketNo']
                name_list = name.split(' ')
                first_name, last_name = name_list[0], name_list[-1]
                username = 'explara' + str(ticket_no)
                tshirt_size = ticket['details']['T-shirt size']
                contact_no = ticket['details']['Contact Number']
                if len(contact_no) > 10:
                    contact_no = contact_no[1:]
            except KeyError as e:
                print("Error in decoding data")
                print(e)
                continue

            # username is intentionally kept as ticket_no so there
            # aren't any chances of DB integrity error of failing UNIQUE
            # constraint on username
            try:
                User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    ticket_id=ticket_no,
                    tshirt_size=tshirt_size,
                    contact=contact_no
                )
            except Exception as e:
                print("Cannot create User because: " + str(e))
                print("Ticket details for failed user creation entry: ")
                print(ticket)
                continue
