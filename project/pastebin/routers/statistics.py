from django.urls import path

from project.pastebin.views import UserStatisticsView, CountryStatisticsView


urlpatterns = [

    path('users/', UserStatisticsView.as_view(), name='user-statistics'),
    path('countries/', CountryStatisticsView.as_view(), name='countries-statistics')

]