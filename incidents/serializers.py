from rest_framework import serializers
from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'
    def validate_severity(self, value):
        allowed = ['Low', 'Medium', 'High']
        if value not in allowed:
            raise serializers.ValidationError("Severity must be Low, Medium, or High.")
        return value