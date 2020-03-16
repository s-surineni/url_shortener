from rest_framework import serializers
from url_shortner_app.models import AccessedTime, ShortURL


class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['created', 'actual_url', 'short_url']

    def create(self, validated_data):
        """
        Create and return a new `ShortURL` instance, given the validated data.
        """
        return ShortURL.objects.create(**validated_data)


class AccessedTimeSerializer(serializers.ModelSerializer):
    short_URL = serializers.StringRelatedField(many=True)

    class Meta:
        model = AccessedTime
        fields = ['accessed', 'short_URL']
