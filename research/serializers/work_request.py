from rest_framework.serializers import ModelSerializer
from ..models import WorkRequest

class BaseWorkRequestSerializer(ModelSerializer):

    class Meta:
        model = WorkRequest
        fields = '__all__'
