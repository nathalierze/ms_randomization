from rest_framework import serializers

from .models import schueler, sitzungssummary


class schuelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = schueler
        fields = '__all__'

class interventiongroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = schueler
        fields = ['interventiongroup']

class sitzungssummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = sitzungssummary
        fields = '__all__'

