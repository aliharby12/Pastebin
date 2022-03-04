from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from project.pastebin.serializers import PasteSerializer
from project.pastebin.models import Paste
from project.pastebin.utils import ErrorResponse, SuccessResponse


class PasteListView(ListAPIView):
    """
    An end point to get all pastes
    """
    serializer_class = PasteSerializer
    def get_queryset(self):
        try:
            queryset = Paste.objects.select_related('user')
            return queryset
        except:
            return ErrorResponse._render(message='No active pastes!')


class MyPasteListView(ListAPIView):
    """
    An end point to get all my pastes
    """
    serializer_class = PasteSerializer
    def get_queryset(self):
        try:
            queryset = Paste.objects.filter(user=self.request.user).select_related('user')
            return queryset
        except:
            return ErrorResponse._render(message='You have no active pastes!')


class PasteDetailView(ListAPIView):
    """
    An end point to get a paste details
    """
    def get(self, request : Request, slug : str, format=None) -> Response:
        try:
            paste = Paste.objects.get(slug=slug)
            if paste.accessed >= 1 and paste.destroyable:
                paste.delete()
            else:
                paste.accessed += 1
                paste.save()
            serializer = PasteSerializer(paste, context={"request": request})
            return SuccessResponse._render(serializer.data)
        except:
            return ErrorResponse._render(message='No active paste with this slug!')
