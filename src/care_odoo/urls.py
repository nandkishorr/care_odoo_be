from django.conf import settings
from django.http import JsonResponse
from django.urls import path

def ping(request):
    return JsonResponse({"status": "OK"})

urlpatterns = [path("ping/", ping, name="ping")]
