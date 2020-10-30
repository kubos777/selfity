from django.shortcuts import render
from rest_framework import permissions,status, exceptions
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import Test, User
from .serializers import TestSerializer, UserSerializer, UserTelephoneSerializer
from .utils import generate_access_token
from django.contrib.auth import authenticate

from django.shortcuts import get_object_or_404

from .sms_api import get_code
from .redis_cache import create_tmp_code, set_session, session_exists, code_exists


from django.contrib.auth import login


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
