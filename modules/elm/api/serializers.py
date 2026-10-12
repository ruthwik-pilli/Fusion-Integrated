from rest_framework import serializers

from modules.elm.models import LeaveRequest


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = "__all__"
