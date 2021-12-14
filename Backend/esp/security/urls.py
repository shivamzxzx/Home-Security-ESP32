from django.urls import path

from security.views import AlertView

urlpatterns = [
    path("alert/<str:alert_status>", AlertView.as_view(), name="alert_view"),
]
