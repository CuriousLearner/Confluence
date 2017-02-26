import datetime
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, UserAttendance

from confluence.settings import TICKET_PALTFORM_CHOICES_REVERSED


logger = logging.getLogger(__name__)


@csrf_exempt
def mark_attendance(request, ticketing_platform):
    ticket_id = request.POST.get('ticket_id')
    logger.info("Ticketing Platform: " + str(ticketing_platform))
    logger.info("Ticket ID: " + str(ticket_id))
    ticketing_platform = TICKET_PALTFORM_CHOICES_REVERSED[ticketing_platform]
    try:
        user = User.objects.get(ticket_id=ticket_id, ticketing_platform=ticketing_platform)
    except User.DoesNotExist:
        logger.warning("User does not exist with given ticket")
        return JsonResponse({"message": "ticket_id does not exist"}, status=404)

    attendance, message = get_attendance_for_user(user)
    logger.info(attendance)
    return JsonResponse({"message": message}, status=200)


def get_attendance_for_user(user):
    """ Get or create the attendance object for user and return the
    respective message.
    """
    now = datetime.datetime.today()
    attendance, created = UserAttendance.objects.get_or_create(
        user=user, attended_on=now
    )
    if created:
        message = "attendance marked for today"
    else:
        message = "attendance already marked for today."
    return attendance, message
