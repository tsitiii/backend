
#this is where the actual password and username are submitted😂😭
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # token['password'] = user.password

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

#available routes in our API
@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)