from rest_framework.generics import ListAPIView
from django.db.models import Count

from project.pastebin.serializers import UserStatisticSerializer, CountryStatisticSerializer
from project.pastebin.utils import ErrorResponse
from project.pastebin.models import User, Country


class UserStatisticsView(ListAPIView):
    """
    An end point to get statistics
    about the top 5 users (username and pastes count)
    """
    serializer_class = UserStatisticSerializer
    def get_queryset(self):
        try:
            queryset = User.objects.annotate(pastes_count=Count('pastes')).order_by('-pastes_count')[:5]
            return queryset
        except:
            return ErrorResponse._render(message='No active pastes!')


class CountryStatisticsView(ListAPIView):
    """
    An end point to get statistics about
    top 5 countries (based on their users' paste count)
    """
    serializer_class = CountryStatisticSerializer
    def get_queryset(self):
        try:
            queryset = Country.objects.annotate(pastes_count=Count('users__pastes')).order_by('-pastes_count')[:5]
            return queryset
        except:
            return ErrorResponse._render(message='No active countries!')