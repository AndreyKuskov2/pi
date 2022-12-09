from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

# Create your views here.

def hello(request):
	return HttpResponse("Hello world!")


class MenuList(APIView):

	def get(self, request, format=None):
		menus = models.Menu.objects.all()
		serializer = serializers.MenuSerializer(menus, many=True)
		return Response(serializer.data)