from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.tokens import RefreshToken
from typing import Any,Dict
from django.contrib.auth import get_user_model


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Override TokenObtainPairSerializer to add extra responses"""
    def validate(self, attrs : Any) -> Dict[str,Any] :
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    """serializer to refresh user token"""
    def validate(self, attrs : Any) -> Dict[str,Any]:
        data = super().validate(attrs)
        decoded_payload = token_backend.decode(data['access'], verify=True)
        user_id=decoded_payload['user_id']
        user = get_user_model().objects.get(id=user_id)
        refresh = RefreshToken.for_user(user)
        data['refresh'] = str(refresh)
        return data