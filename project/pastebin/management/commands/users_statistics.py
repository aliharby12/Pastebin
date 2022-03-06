from django.core.management.base import BaseCommand
from django.db.models import Count

from project.pastebin.models import User

class Command(BaseCommand):
    help = 'user statistics'

    def handle(self, *args, **kwargs):
        users = User.objects.annotate(
            pastes_count=Count('pastes')).order_by(
                '-pastes_count')[:5].values(*['id', 'pastes_count', 'username'])
        [print(user) for user in users]