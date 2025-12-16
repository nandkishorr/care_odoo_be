from django.http import JsonResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from care_odoo.resources.account.viewset import AccountViewSet
from care_odoo.resources.payment_method.viewset import PaymentMethodViewSet


def ping(request):
    return JsonResponse({"status": "OK"})


router = DefaultRouter()
router.register("payment-method", PaymentMethodViewSet, basename="payment-method")
router.register("account", AccountViewSet, basename="account")

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("", include(router.urls)),
]
