from django.core.management.base import BaseCommand

from project.pastebin.models import Paste


class Command(BaseCommand):
    help = 'Displays all pastes'

    def handle(self, *args, **kwargs):
        pastes = Paste.objects.values(*['id', 'text', 'slug', 'name', 'user', 'accessed'])
        [print(paste) for paste in pastes]