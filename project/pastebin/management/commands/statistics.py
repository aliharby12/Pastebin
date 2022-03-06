from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.models import Count


class Command(BaseCommand):
    help = 'Displays all pastes'

    def handle(self, *args, **kwargs):
        users = get_user_model().objects.annotate(
            pastes_count=Count('pastes')).order_by(
                '-pastes_count')[:5].values(*['id', 'pastes_count', 'username'])
        [print(user) for user in users]