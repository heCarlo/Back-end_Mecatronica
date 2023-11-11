from django.urls import path
from app.views.sensors.receiveSensorDataView import ReceiveSensorDataView
from app.views.users.listUserView import ListUserView
from app.views.users.createUserView import CreateUserView
from app.views.users.updateUserView import UpdateUserView
from app.views.users.getUserView import GetUserView
from app.views.users.deleteUserView import DeleteUserView

urlpatterns = [
    path('users/', ListUserView.as_view(), name='user-list'),
    path('users/create/', CreateUserView.as_view(), name='user-create'),
    path('users/<int:pk>/', GetUserView.as_view(), name='user-retrieve'),
    path('users/<int:pk>/update/', UpdateUserView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', DeleteUserView.as_view(), name='user-delete'),
    path('receive-sensor-data/', ReceiveSensorDataView.as_view(), name='receive_sensor_data'),
]
