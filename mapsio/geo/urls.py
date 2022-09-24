from django.urls import path
from . import views

urlpatterns = [
    path("<str:dev>/", views.GetGeoDataPacketsByDev.as_view())
]
