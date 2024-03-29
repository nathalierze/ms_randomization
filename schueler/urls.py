from django.urls import path

from .views import SitzungssummaryViewSet

urlpatterns = [
    path(
        "interventiongroup/<str:pk>",
        SitzungssummaryViewSet.as_view({"get": "get_interventiongroup"}),
    )
]
