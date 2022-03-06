from django.core.management.base import BaseCommand
from django.db.models import Count

from project.pastebin.models import Country

class Command(BaseCommand):
    help = 'countries statistics'

    def handle(self, *args, **kwargs):
        countries = Country.objects.annotate(
            pastes_count=Count('users__pastes')).order_by(
                '-pastes_count')[:5].values(*['id', 'pastes_count', 'title'])
        [print(country) for country in countries]