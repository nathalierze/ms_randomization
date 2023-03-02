from rest_framework import serializers

from .models import schueler, sitzungssummary, gast


class SchuelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = schueler
        fields = "__all__"


class InterventiongroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = schueler
        fields = ["interventiongroup"]


class SitzungssummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = sitzungssummary
        fields = "__all__"


class GastSerializer(serializers.ModelSerializer):
    class Meta:
        model = gast
        fields = "__all__"
