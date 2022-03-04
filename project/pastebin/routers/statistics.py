from django.urls import path

from project.pastebin.views import PasteStatisticsView


urlpatterns = [

    path('', PasteStatisticsView.as_view())

]