from django.urls import path, include
from .views import (
	HomeView,
	EventDetailView,
	AboutView,
	ContactView,
	SchoolView,
)

app_name = 'event'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('school/', SchoolView.as_view(), name='school'),
    path('vacancies/', include('vacancy.urls', namespace='vacancy')),
    path('<str:slug>/', EventDetailView.as_view(), name='event'),
]