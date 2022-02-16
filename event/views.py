from django.shortcuts import render
from django.views.generic import View
from .models import Event


class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
    	events = Event.objects.all()
    	context = {'events': events}
    	return render(request, self.template_name, context)


class EventDetailView(View):
	model = Event
	queryset = Event.objects.all()
	template_name = 'event_detail_view.html'
	pk_url_kwarg = 'slug'


	def get(self, request, slug):
		event = Event.objects.get(slug=slug)

		context = {'event': event}
		return render(request, self.template_name, context)


