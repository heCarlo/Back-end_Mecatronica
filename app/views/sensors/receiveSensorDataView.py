from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models.sensors.sensorEntity import SensorData
from app.serializers.sensorDataSerializer import SensorDataSerializer

class ReceiveSensorDataView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = SensorDataSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'Data received successfully!'}, status=status.HTTP_201_CREATED)
            return Response({'status': 'Invalid data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': 'Error receiving data', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        try:
            sensor_data = SensorData.objects.all()
            serializer = SensorDataSerializer(sensor_data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'Error getting data', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
