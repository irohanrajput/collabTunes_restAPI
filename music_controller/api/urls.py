from django.urls import path
from .views import *

urlpatterns = [
    path('home/', RoomView.as_view()),
]
