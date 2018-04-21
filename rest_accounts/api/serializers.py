from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_accounts.api.serializers import *
User = get_user_model()


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('url', 'username', 'email', 'is_staff')


class MpesaB2CSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MpesaC2BSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MpesaAccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MpesaReversalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
