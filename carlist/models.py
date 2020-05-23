from django.db import models

class Car(models.Model):
	MECHANIC = 1
	AUTOMATIC = 2
	ROBOT = 3

	transmission_choices = [
		(MECHANIC, 'Механическая'),
		(AUTOMATIC, 'Автомат'),
		(ROBOT, 'Робот')
	]

	manufacturer = models.CharField( "Производитель", max_length=100)
	car_model = models.CharField( "Модель автомобиля", max_length=100)
	year = models.IntegerField("Год выпуска")
	transmission = models.SmallIntegerField("Коробка передач", choices=transmission_choices)
	color = models.CharField( "Цвет", max_length=100)

	def __str__(self):
		return self.car_model