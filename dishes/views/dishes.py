from rest_framework.viewsets import ModelViewSet

from clients.permissions import IsTeacherPermission
from utils.paginations import SelectorPagination
from ..models import Dishes
from ..serializers import BaseDishesSerializer

class DishesModelViewSet (
    ModelViewSet,
):
    queryset = Dishes.objects.all()
    serializer_class = BaseDishesSerializer
    permission_classes = [
        IsTeacherPermission
    ]
    pagination_class = SelectorPagination
