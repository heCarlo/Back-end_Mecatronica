from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models.sensors.sensorEntity import SensorData
from app.serializers.sensorDataSerializer import SensorDataSerializer
from app.swaggers.sensors.ReceiveSensorDataSchema import (
    receive_sensor_data_post_schema,
    receive_sensor_data_get_schema,
    receive_sensor_data_put_schema,
    receive_sensor_data_delete_schema,
    receive_sensor_data_get_by_id_schema,
)


class ReceiveSensorDataPostView(APIView):
    @receive_sensor_data_post_schema
    def post(self, request, *args, **kwargs):
        try:
            serializer = SensorDataSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "Data received successfully!"},
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                {"status": "Invalid data", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"status": "Error receiving data", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ReceiveSensorDataGetView(APIView):
    @receive_sensor_data_get_schema
    def get(self, request, *args, **kwargs):
        try:
            sensor_data = SensorData.objects.all()
            serializer = SensorDataSerializer(sensor_data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"status": "Error getting data", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ReceiveSensorDataPutView(APIView):
    @receive_sensor_data_put_schema
    def put(self, request, *args, **kwargs):
        try:
            instance = SensorData.objects.get(id=kwargs.get("pk"))
            serializer = SensorDataSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "Data updated successfully!"}, status=status.HTTP_200_OK
                )
            return Response(
                {"status": "Invalid data", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except SensorData.DoesNotExist:
            return Response(
                {"status": "Data not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"status": "Error updating data", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ReceiveSensorDataDeleteView(APIView):
    @receive_sensor_data_delete_schema
    def delete(self, request, *args, **kwargs):
        try:
            instance = SensorData.objects.get(id=kwargs.get("pk"))
            instance.delete()
            return Response(
                {"status": "Data deleted successfully!"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except SensorData.DoesNotExist:
            return Response(
                {"status": "Data not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"status": "Error deleting data", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ReceiveSensorDataGetByIdView(APIView):
    @receive_sensor_data_get_by_id_schema
    def get(self, request, pk, *args, **kwargs):
        try:
            instance = SensorData.objects.get(id=pk)
            serializer = SensorDataSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SensorData.DoesNotExist:
            return Response(
                {"status": "Data not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"status": "Error getting data by ID", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
