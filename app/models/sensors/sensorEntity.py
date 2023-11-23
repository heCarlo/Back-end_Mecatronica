from django.db import models

class SensorData(models.Model):
    sensort = models.FloatField()
    servo_vertical = models.FloatField()
    secury_mode = models.BooleanField()

    def __str__(self):
        return f'SensorData - {self.timestamp}'
