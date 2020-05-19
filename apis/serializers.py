from rest_framework import serializers
from .models import Member, Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'start_time',
            'end_time',
        )
        model = Activity


class MemberSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'real_name',
            'tz',
            'activities',
    
        )
        model = Member
