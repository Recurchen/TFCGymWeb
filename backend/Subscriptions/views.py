from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .serializers import PlanSerializer
from django.contrib.auth.models import User
from .models import Plan, Subscription

class PlansView(ListAPIView):
    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.all()


# # Create your views here.
# class CreateSubView(APIView):
#     def post(self, request):
