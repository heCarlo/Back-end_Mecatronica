from rest_framework import serializers
from app.models.sensors.sensorEntity import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'
