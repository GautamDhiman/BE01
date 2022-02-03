from .views import TaskApiView, TaskDetails
from django.urls import path

urlpatterns = [
    path('api/v1/', TaskApiView.as_view()),
    path('api/v1/<int:id>/', TaskDetails.as_view()),
]