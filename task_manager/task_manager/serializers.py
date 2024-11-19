from rest_framework import serializers
from .models import Task
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date']

    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def validate_status(self, value):
        if value not in ['pending', 'in_progress', 'completed']:
            raise serializers.ValidationError("Invalid status.")
        return value