from django.urls import path, include

from project.pastebin.views import MyPasteListView, PasteDetailView, PasteListView, CreatePasteView


urlpatterns = [

    path('', PasteListView.as_view(), name='all-pastes'),
    path('create/', CreatePasteView.as_view(), name='create-paste'),
    path('my-pastes/', MyPasteListView.as_view(), name='my-pastes'),
    path('<slug:slug>/', PasteDetailView.as_view(), name='paste-detail')

]