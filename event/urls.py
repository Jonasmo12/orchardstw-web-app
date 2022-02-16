from django.urls import path
from .views import (
	HomeView,
	EventDetailView,
)

app_name = 'event'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:slug>/', EventDetailView.as_view(), name='event'),
]