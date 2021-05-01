from django.db import models

# Create your models here.


PIZZA_TYPE = (
	("Regular", "Regular"),
	("Square", "Square"),
)

PIZZA_SIZE = (
	("S", "Small"),
	("M", "Medium"),
	("L", "Large"),
	("XL", "Extra Large"),
)


class Toppings(models.Model):
	user = models.ForeignKey('core.User', on_delete=models.PROTECT)
	name = models.CharField(max_length=180, null=True, blank=True)

	def __str__(self):
		return str(self.name)


class Pizza(models.Model):
	user = models.ForeignKey('core.User', on_delete=models.PROTECT)
	name = models.CharField(max_length=180, null=True, blank=True)
	toppings = models.ManyToManyField(Toppings)
	pizza_type = models.CharField(max_length=8, choices=PIZZA_TYPE)
	size = models.CharField(max_length=8, choices=PIZZA_SIZE)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.name)
