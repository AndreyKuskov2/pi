from rest_framework import serializers

from . import models

class MenuSerializer(serializers.ModelSerializer):
	category = serializers.CharField(source="category.name", max_length=128)

	class Meta():
		model = models.Menu
		fields = ["name", "description", "image", "price", "category"]