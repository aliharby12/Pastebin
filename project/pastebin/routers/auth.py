from django.urls import path

from project.pastebin.views import GithubLoginView, CreateUserView, TokenAPIView, TokenRefreshAPIView


urlpatterns = [

    path('github/', GithubLoginView.as_view(), name='github_login'),
    path('register/', CreateUserView.as_view(), name='user-register'),
    path('login-with-token/', TokenAPIView.as_view(), name='login-with-token'),
    path('refresh-token/', TokenRefreshAPIView.as_view(), name='token-refresh')
]