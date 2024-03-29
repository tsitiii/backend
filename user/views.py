from djoser.views import TokenCreateView
from .serializers import * 
class UserLoginView(TokenCreateView):
    serializer_class = UserLoginSerializer



