from django.db import router
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView
from .views import PlansView, CreateSubView, CancelSubView, PaymentHistoryView
# from .views import ProfileAPI

app_name = 'subscriptions'

urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('plans/', PlansView.as_view()),
    path('users/<user_id>/add', CreateSubView.as_view()),
    path('users/<user_id>/cancel', CancelSubView.as_view()),
    path('users/<user_id>/payment_history', PaymentHistoryView.as_view())
]