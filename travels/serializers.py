from rest_framework import serializers
from .models import TravelCategory, TravelPost


class TravelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelCategory
        fields = '__all__'

class TravelPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPost
        fields = '__all__'
