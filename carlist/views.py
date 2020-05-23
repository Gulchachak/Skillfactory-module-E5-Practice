from django.db.models import Q
from django.views.generic import TemplateView
from carlist.models import Car


class CarView(TemplateView):
	template_name = 'car_list.html'

	def get_context_data(self, **kwargs):
		my_dict = self.request.GET
		or_condition = Q()
		for key, value in my_dict.items():
			if value and key in vars(Car):
				or_condition.add(Q(**{key: value}), Q.AND)
		return {'cars': Car.objects.filter(or_condition)}

#	def get_queryset(self):
#		query = self.request.GET.get('q')
#		if query:
#			cars = Car.objects.filter(
#				Q(manufacturer__icontains='query') | 
#				Q(car_model__icontains='query') |
#				Q(year__icontains='query') |
#				Q(transmission__icontains=Car.transmission_choice(query)) |
#				Q(color__icontains='query')
#		)
#		else:
#			cars = Car.objects.all()
#		return cars