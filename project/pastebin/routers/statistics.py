from django.urls import path

from project.pastebin.views import UserStatisticsView


urlpatterns = [

    path('', UserStatisticsView.as_view())

]