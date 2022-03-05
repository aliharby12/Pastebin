from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from django.db.models import Count

from project.pastebin.serializers import UserStatisticSerializer
from project.pastebin.utils import ErrorResponse


class UserStatisticsView(ListAPIView):
    """
    An end point to get statistics
    """
    serializer_class = UserStatisticSerializer
    def get_queryset(self):
        try:
            queryset = get_user_model().objects.annotate(pastes_count=Count('pastes')).order_by('-pastes_count')[:5]
            return queryset
        except:
            return ErrorResponse._render(message='No active pastes!')