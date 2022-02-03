from .views import TaskApiView, TaskDetails, RegisterUser
from django.urls import path

urlpatterns = [
    path('api/v1/', TaskApiView.as_view()),
    path('api/v1/<int:id>/', TaskDetails.as_view()),
    path('register/', RegisterUser.as_view())
]