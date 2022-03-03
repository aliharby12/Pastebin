from rest_framework.serializers import ModelSerializer

from project.pastebin.models import Paste


class PasteSerializer(ModelSerializer):
    """serialize the paste data"""

    class Meta:
        model = Paste
        exclude = ('created', 'modified',)
        read_only_fields = ('user',)