from django.urls import path
from . import views

app_name = 'api_app'

urlpatterns = [
    path('api/test', views.TestList.as_view()),
]