import datetime
import jwt
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

def generate_access_token(user):
    refresh = RefreshToken.for_user(user)
    pair_tokens =  {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return pair_tokens['access']
