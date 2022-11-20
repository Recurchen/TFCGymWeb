from django.db import router
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView
from .views import PlansView
# from .views import ProfileAPI

app_name = 'subscriptions'

urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('plans/', PlansView.as_view()),
]
