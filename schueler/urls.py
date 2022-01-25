from django.urls import path

from .views import SchuelerViewSet

urlpatterns = [
    path('schueler', SchuelerViewSet.as_view({
        'get':'list',
        'post': 'create'
    })),
    path('schueler/<str:pk>', SchuelerViewSet.as_view({
        'get': 'retrieve'
    }))
]