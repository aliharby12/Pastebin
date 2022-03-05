from rest_framework.serializers import ModelSerializer, IntegerField

from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class UserStatisticSerializer(ModelSerializer):
    """serialize the user statistics"""
    pastes_count = IntegerField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'pastes_count',)