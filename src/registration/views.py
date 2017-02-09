import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
from .models import User, UserAttendance

from confluence.settings import TICKET_PALTFORM_CHOICES_REVERSED


logger = logging.getLogger(__name__)


@csrf_exempt
def mark_attendance(request, ticketing_platform):

    request = json.load(request)
    ticket_id = request["ticket_id"]
    now = datetime.today()
    try:
        logger.info("Ticketing Platform: " + str(ticketing_platform))
        logger.info("Ticket ID: " + str(ticket_id))
        ticketing_platform = TICKET_PALTFORM_CHOICES_REVERSED[ticketing_platform]
        user = User.objects.get(ticket_id=ticket_id, ticketing_platform=ticketing_platform)
    except User.DoesNotExist:
        logger.warning("User does not exist with given ticket")
        return JsonResponse({"error": "ticket_id does not exist"}, status=404)

    attendance = UserAttendance.objects.get_or_create(
        user=user, attended_on=now
    )
    logger.info(attendance)
    return JsonResponse({"message": "attendance marked for today"}, status=200)
