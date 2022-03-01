from django.shortcuts import render
from django.views.generic import View
from .models import Vacancy
# Create your views here.


class VacancyView(View):
	template_name = 'vacancy.html'
	model = Vacancy

	def get(self, request, *args, **kwargs):
		vacancies = Vacancy.objects.all()
		context = {'vacancies': vacancies}
		return render(request, self.template_name, context)