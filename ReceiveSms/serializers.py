from .models import SmsInfo
from rest_framework import serializers


class SmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmsInfo
        fields = ['id', 'message', 'sender', 'recipient']
