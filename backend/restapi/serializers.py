from rest_framework import serializers
from .models import Ships
from .models import Positions

"""
Creating serializer which maintains relation between ships and it's position
"""


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = ('latitude', 'longitude')


class ShipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ships
        fields = ('imo', 'name')
