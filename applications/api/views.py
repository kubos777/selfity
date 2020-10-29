from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Test
from .serializers import TestSerializer
# Create your views here.

class TestList(ListAPIView):
    serializer_class = TestSerializer
    def get_queryset(self):
        return Test.objects.all()