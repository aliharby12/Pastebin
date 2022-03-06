from django.core.management.base import BaseCommand

from project.pastebin.models import Paste
from project.pastebin.serializers import PasteSerializer


class Command(BaseCommand):
    help = 'Displays a single paste based on the slug'

    def handle(self, *args, **kwargs):
        slug = input('Enter the slug of the paste: ')
        paste = Paste.objects.get(slug=slug)
        print(PasteSerializer(paste).data)