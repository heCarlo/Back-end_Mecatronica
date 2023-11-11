from django.db import models

class SensorData(models.Model):
    angular_displacement = models.FloatField()
    output_voltage = models.FloatField()
    current = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'SensorData - {self.timestamp}'
