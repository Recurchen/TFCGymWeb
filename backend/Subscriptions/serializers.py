from rest_framework import serializers
from .models import Plan, Subscription
from Studios.models import Studio
from Accounts.models import Profile

class PlanSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Plan
        fields = ['name', 'description', 'studio', 'price', 'time_unit', 'time_range','currency']
        required = ['name', 'studio', 'price', 'time_unit',]


class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    plan = PlanSerializer()
    
    class Meta:
        model = Subscription
        fields = ['user', 'plan', 'start_time', 'canceled', 'auto_pay',]
        required = ['user', 'plan']

    def get_user(self,obj):
        user = Profile.objects.user.objects.filter(id=obj.user)
        return user