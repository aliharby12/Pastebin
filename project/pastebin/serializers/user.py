from rest_framework.serializers import ModelSerializer, IntegerField

from project.pastebin.models import User, Country


class UserSerializer(ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = User
        fields = ('username', 'password', 'country')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return User.objects.create_user(**validated_data)


class UserStatisticSerializer(ModelSerializer):
    """serialize the user statistics"""
    pastes_count = IntegerField()

    class Meta:
        model = User
        fields = ('username', 'pastes_count',)


class CountryStatisticSerializer(ModelSerializer):
    """serialize the countries statistics"""
    pastes_count = IntegerField()
    
    class Meta:
        model = Country
        exclude = ('created', 'modified',)