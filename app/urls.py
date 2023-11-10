from django.urls import path
from app.views.userView import UserEntityListView, UserEntityDetailView

urlpatterns = [
    path('users/', UserEntityListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserEntityDetailView.as_view(), name='user-detail'),
]