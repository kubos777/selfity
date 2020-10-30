from django.urls import path
from . import views

app_name = 'api_app'

urlpatterns = [
    path('api/test', views.TestList.as_view()),
    path('api/first/send-sms', views.FirstSendSMS.as_view()),
    path('api/second/return-bearer', views.SecondReturnBearer.as_view()),
    path('api/third/verify-session', views.VerifyActiveSession.as_view()),

    path('api/login',views.Login.as_view()),
]