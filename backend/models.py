from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, verbose_name="Категория")

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

	def __str__(self) -> str:
		return f"{self.name}"

class Menu(models.Model):
	name = models.CharField(max_length=128, verbose_name="Название блюда")
	description = models.TextField(verbose_name="Описание блюда")
	image = models.ImageField(upload_to='photos_of_dishes', verbose_name="Фото блюда")
	price = models.PositiveIntegerField(verbose_name="Цена", default=0)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	class Meta:
		db_table = "Menu"
		verbose_name = "Меню"
		verbose_name_plural = "Меню"

	def __str__(self) -> str:
		return f"Название блюда {self.name}"