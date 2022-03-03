from django.urls import path, include

from project.pastebin.views import MyPasteListView, PasteDetailView


urlpatterns = [

    path('', MyPasteListView.as_view()),
    path('<slug:slug>/', PasteDetailView.as_view())

]