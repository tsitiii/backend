
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,TokenCreateSerializer as loginSerializer
from .models import User

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','first_name','last_name','username','email','password']


# we don't need the ff but just incase...
class UserLoginSerializer(loginSerializer):
    class Meta:
         model=User
         fields=['username', 'password'] #for api 
        
