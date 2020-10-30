from .models import Test, User, Image
from .redis_cache import create_tmp_code, set_session, session_exists, code_exists
from .serializers import (
    TestSerializer, 
    UserSerializer, 
    UserTelephoneSerializer, 
    ImageSerializer, 
    ImagesSerializer,
    HashtagSerializer,
    )
from .sms_api import get_code
from .utils import generate_access_token, get_address
from base64 import b64decode
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import permissions,status, exceptions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid
import io
from PIL import Image as PillowImage

# Create your views here.

class TestList(ListAPIView):
    serializer_class = TestSerializer
    def get_queryset(self):
        return Test.objects.all()


class FirstSendSMS(APIView):
    permission_classes = (AllowAny,)
    def post(self,request,*args,**kwargs):
        telephone = request.data.get('telephone')
        if telephone:
            tel_number = str(telephone)
            user = User.objects.filter(telephone__iexact =tel_number)

            if user.exists() and session_exists(tel_number):
                return Response({
                'status': False,
                'detail': 'El usuario tiene una sesion activa'
            })
            else:
                response,code = get_code(tel_number)
                code_response = response.json().get('msg')
                if code:
                    telephone_code = {
                        "telephone": telephone,
                        "code": code
                    }
                    create_tmp_code(telephone_code)
                    return Response({
                        'status': True,
                        'detail': code_response
                    })
                return Response({
                    'status': False,
                    'detail': 'Error generating code'
                })

        else:
            return Response({
                'status': False,
                'detail': 'Teléfono no ingresado'
            })

class SecondReturnBearer(APIView):

    permission_classes = (AllowAny,)
    def post(self,request,*args,**kwargs):
        telephone = request.data.get('telephone')
        code = request.data.get('code')
        response = Response()
        if telephone and code:
            tel_number = str(telephone)
            user = User.objects.get(telephone__iexact =tel_number)
            print(user)
            print(code_exists(code))
            if user and code_exists(code):
                access_token = generate_access_token(user)
                response.data = {
                    'access_token': access_token,
                    'telephone': telephone,
                }
                set_session(response.data)
                return response
            else:
                return Response({
                'status': False,
                'detail': 'Número o código no existen'
            })

        else:
            return Response({
                'status': False,
                'detail': 'Teléfono o código no ingresados'
            })


class VerifyActiveSession(APIView):
    def post(self,request,*args,**kwargs):
        telephone = request.data.get('telephone')
        if telephone:
            tel_number = str(telephone)
            user = User.objects.filter(telephone__iexact =tel_number)
            if user.exists() and session_exists(tel_number):
                return Response({
                'status': False,
                'detail': 'El usuario tiene una sesión activa'
            })
            else:
                return Response({
                    'status': False,
                    'detail': 'Sin sesión activa'
                })

        else:
            return Response({
                'status': False,
                'detail': 'Teléfono no ingresado'
            })

class UploadImageBase64(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):        
        received = request.data       
        newImage = Image()
        newImage.hashtag = received['hashtag']
        newImage.coords = received['coords']
        img_received = received['file']
        img_received_ext = img_received.split(';')
        img_received_ext = img_received_ext[0].split(':')
        img_received_ext = img_received_ext[1].split('/')
        img_received_ext = img_received_ext[1]
        newImage.MIMEType = img_received_ext
        clear_image_data = img_received.replace('data:image/'+img_received_ext+';base64,','')
        image_data = b64decode(clear_image_data)
        image_name = str(uuid.uuid4()) + '.' + str(img_received_ext)
        newImage.file = ContentFile(image_data, image_name )
        image = PillowImage.open(newImage.file)
        image_io = io.BytesIO()
        image  = image.resize((90,90), PillowImage.ANTIALIAS)
        image.save(image_io, format=img_received_ext)
        newImage.thumbnail = ContentFile(image_io.getvalue(),image_name)
        print(str(uuid.uuid4()) + '.' + str(img_received_ext))
        try:
            newImage.save()
            return Response({
                "status": True,
                "detail": 'Imagen guardada correctamente'
            })
        except:
            return Response({
                "status": True,
                "detail": 'Imagen no guardada'
            })


class DataThumbnail(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ImageSerializer
    def get_queryset(self):
        hashtag = self.kwargs['hashtag']
        return  Image.objects.filter(hashtag=hashtag)


class ImagesList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ImagesSerializer
    def get_queryset(self):
        return  Image.objects.all()


class HashtagsList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = HashtagSerializer
    def get_queryset(self):
        return  Image.objects.all()

class Login(APIView):
    permission_classes = [permissions.AllowAny, ]
    def post(self, request, format=None):
        telephone = request.data.get("telephone")
        password = request.data.get("password")
        response = Response()
        user = authenticate(request,telephone=telephone,password=password)
        print(user)
        if user is not None:
            #login(request,user)
            serialized_user_telephone = UserTelephoneSerializer(user).data['telephone']
            access_token = generate_access_token(user)
            response.data = {
                    'access_token': access_token,
                    'telephone': serialized_user_telephone,
                }
            set_session(response.data)
            return response
        else :
            return Response('No')
