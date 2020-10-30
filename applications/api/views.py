from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Test, User
from .serializers import TestSerializer

from django.shortcuts import get_object_or_404

from .sms_api import get_code
from .redis_cache import create_tmp_code
# Create your views here.

class TestList(ListAPIView):
    serializer_class = TestSerializer
    def get_queryset(self):
        return Test.objects.all()


class ValidateTelephone(APIView):

    def post(self,request,*args,**kwargs):
        
        telephone = request.data.get('telephone')
        print(request.data)
        if telephone:
            tel_number = str(telephone)
            user = User.objects.filter(telephone__iexact =tel_number)
            if user.exists():
                return Response({
                'status': False,
                'detail': 'El télefono ya existe'
            })
            else:
                response,code = get_code(tel_number)
                if code:
                    telephone_code = {
                        "telephone": telephone,
                        "code": code
                    }
                    create_tmp_code(telephone_code)

                    return Response({
                        'status': True,
                        'detail': response
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


