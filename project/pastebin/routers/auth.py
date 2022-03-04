from django.urls import path

from project.pastebin.views import GithubLoginView


urlpatterns = [

    path('dj-rest-auth/github/', GithubLoginView.as_view(), name='github_login')

]