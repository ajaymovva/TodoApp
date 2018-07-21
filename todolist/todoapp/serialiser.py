from rest_framework import routers, serializers, viewsets
from todoapp.models import *


class TodoSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Todo_info
        fields = ('task_title', 'task_info', 'actual_date', 'status')


