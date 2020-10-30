from rest_framework_simplejwt.tokens import RefreshToken
from geopy.geocoders import Nominatim
def generate_access_token(user):
    refresh = RefreshToken.for_user(user)
    pair_tokens =  {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return pair_tokens['access']

   
def get_address(coords):
    coords = coords.replace(";",",")
    geolocator = Nominatim(user_agent="api_app")
    location = geolocator.reverse(coords)
    return location

