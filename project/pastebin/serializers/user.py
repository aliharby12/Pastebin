from rest_framework.serializers import ModelSerializer, IntegerField

from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    """serialize the user data"""
    pastes_count = IntegerField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'pastes_count',)