from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from ..models.dishes import Dishes

class BaseDishesSerializer(ModelSerializer):
    class Meta:
        model = Dishes
        fields = '__all__'
