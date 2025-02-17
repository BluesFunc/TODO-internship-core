from rest_framework import serializers


class DeadlineSerializer(serializers.BaseSerializer):
    deadline = serializers.DateTimeField()
