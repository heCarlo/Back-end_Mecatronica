# Arquivo: swagger_schemas.py
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

receive_sensor_data_post_schema = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'angular_displacement': openapi.Schema(type=openapi.TYPE_NUMBER),
            'output_voltage': openapi.Schema(type=openapi.TYPE_NUMBER),
            'current': openapi.Schema(type=openapi.TYPE_NUMBER),
        },
        required=['angular_displacement', 'output_voltage', 'current']
    ),
    responses={
        201: 'Data received successfully!',
        400: 'Invalid data',
        500: 'Error receiving data',
    },
)

receive_sensor_data_get_schema = swagger_auto_schema(
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'angular_displacement': openapi.Schema(type=openapi.TYPE_NUMBER),
                    'output_voltage': openapi.Schema(type=openapi.TYPE_NUMBER),
                    'current': openapi.Schema(type=openapi.TYPE_NUMBER),
                    'timestamp': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                }
            )
        ),
        500: 'Error getting data',
    },
)

receive_sensor_data_put_schema = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'angular_displacement': openapi.Schema(type=openapi.TYPE_NUMBER),
            'output_voltage': openapi.Schema(type=openapi.TYPE_NUMBER),
            'current': openapi.Schema(type=openapi.TYPE_NUMBER),
        },
        required=['id', 'angular_displacement', 'output_voltage', 'current']
    ),
    responses={
        200: 'Data updated successfully!',
        400: 'Invalid data',
        404: 'Data not found',
        500: 'Error updating data',
    },
)

receive_sensor_data_delete_schema = swagger_auto_schema(
    responses={
        204: 'Data deleted successfully!',
        404: 'Data not found',
        500: 'Error deleting data',
    },
)

receive_sensor_data_get_by_id_schema = swagger_auto_schema(
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'angular_displacement': openapi.Schema(type=openapi.TYPE_NUMBER),
                'output_voltage': openapi.Schema(type=openapi.TYPE_NUMBER),
                'current': openapi.Schema(type=openapi.TYPE_NUMBER),
                'timestamp': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            }
        ),
        404: 'Data not found',
        500: 'Error getting data by ID',
    },
)

