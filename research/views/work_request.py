from rest_framework.viewsets import ModelViewSet
from clients.permissions import IsAssistantPermission
from utils.paginations import SelectorPagination
from ..models import Research
from ..serializers.work_request import BaseWorkRequestSerializer


class WorkRequestModelViewSet (
    ModelViewSet,
):
    queryset = Research.objects.all()
    serializer_class = BaseWorkRequestSerializer
    permission_classes = [
        IsAssistantPermission
    ]
    pagination_class = SelectorPagination
