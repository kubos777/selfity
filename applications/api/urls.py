from django.urls import path
from . import views

app_name = 'api_app'

urlpatterns = [
    path('api/test', views.TestList.as_view()),
    path('api/first/send-sms', views.FirstSendSMS.as_view()),
    path('api/second/return-bearer', views.SecondReturnBearer.as_view()),
    path('api/third/verify-session', views.VerifyActiveSession.as_view()),
    path('api/fourth/upload-image',views.UploadImageBase64.as_view()),
    path('api/fifth/data-thumbnail/<hashtag>',views.DataThumbnail.as_view()),
    path('api/sixth/images/list',views.ImagesList.as_view()),
    path('api/seventh/hastags/list',views.HashtagsList.as_view()),
    path('api/login',views.Login.as_view()),
]
