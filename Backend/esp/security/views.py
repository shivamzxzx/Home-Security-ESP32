import datetime
import os

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from security.alert_sender import Alert
from security.models import AlertLog
import environ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialise environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

AUTH_KEY = env('AUTH_KEY')
RECEIVERS_NUMBERS = env('RECEIVERS_NUMBERS', default=[])


class AlertView(
    generics.GenericAPIView,
):
    """
    The authentication schemes are always defined as a list of classes. REST framework will attempt to authenticate
    with each class in the list, and will set request.user and request.auth using the return value
    of the first class that successfully authenticates.
    """
    # authentication_classes = [
    #     TokenAuthentication,
    # ]
    #
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Create a reports request by selecting a specific report from canned reports
        """
        try:
            alert = self.kwargs.get('alert_status')
            if alert == 'True' or alert == 'true':
                created_time = datetime.datetime.now() - datetime.timedelta(minutes=10)
                if not AlertLog.objects.filter(created_at__gte=created_time, status='Success').exists():
                    alert_instance = Alert(AUTH_KEY, RECEIVERS_NUMBERS, "INTRUDER ALERT!!")
                    response = alert_instance.send_sms()
                    print(response.text)
                    AlertLog.objects.create(text=response.text, response=response.json(), status='Success')
                    return Response(response.text, status=status.HTTP_200_OK)
                else:
                    return Response("Alert already sent!!", status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            AlertLog.objects.create(response=e.args[0], status='Failed')
            return Response(data="Something went wrong", status=status.HTTP_500_INTERNAL_SERVER_ERROR)