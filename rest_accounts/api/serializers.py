from django.contrib.auth import get_user_model

from rest_framework import serializers
User = get_user_model()


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('url', 'username', 'email', 'is_staff')
