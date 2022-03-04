from django.urls import path, include

from project.pastebin.views import MyPasteListView, PasteDetailView, PasteListView


urlpatterns = [

    path('', PasteListView.as_view()),
    path('my-pastes/', MyPasteListView.as_view()),
    path('<slug:slug>/', PasteDetailView.as_view())

]