from rest_framework import serializers

from .models import schueler


class schuelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = schueler
        fields = '__all__'