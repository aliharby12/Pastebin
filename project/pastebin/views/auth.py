from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from project.pastebin.serializers import MyTokenObtainPairSerializer, MyTokenRefreshSerializer

from project.pastebin.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class GithubLoginView(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/github/login/callback/'
    client_class = OAuth2Client


class TokenAPIView(TokenObtainPairView):
    """
    An end point for the user token
    """
    serializer_class = MyTokenObtainPairSerializer


class TokenRefreshAPIView(TokenRefreshView):
    """
    An end point to refresh the user token
    """
    serializer_class = MyTokenRefreshSerializer