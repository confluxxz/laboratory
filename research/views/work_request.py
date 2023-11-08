from rest_framework.viewsets import ModelViewSet
from clients.permissions import IsTeacherPermission, IsStudentPermission
from utils.paginations import SelectorPagination
from ..models import WorkRequest
from ..serializers.work_request import BaseWorkRequestStudentSerializer, BaseWorkRequestTeacherSerializer, BaseWorkRequestApprovedSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from utils.serializers import ACTIONS

class WorkRequestTeacherModelViewSet(
    ModelViewSet
):
    queryset = WorkRequest.objects.all()
    serializer_class = BaseWorkRequestTeacherSerializer
    permission_classes = [
        IsTeacherPermission
    ]
    pagination_class = SelectorPagination


class WorkRequestStudentModelViewSet(
    ModelViewSet
):
    queryset = WorkRequest.objects.all()
    serializer_class = BaseWorkRequestStudentSerializer
    serializers_class = {
        ACTIONS.CREATE: BaseWorkRequestStudentSerializer,
    }
    permission_classes = [
        IsStudentPermission
    ]
    pagination_class = SelectorPagination

class WorkRequestTeacherApprovedModelViewSet(
    ModelViewSet
):
    queryset = WorkRequest.objects.all()
    serializer_class = BaseWorkRequestApprovedSerializer
    permission_classes = [
        IsTeacherPermission
    ]
    pagination_class = SelectorPagination

    @action(methods=['POST'], detail=True, url_path='take')
    def take(self, request, *args, **kwargs):
        if not self.is_approved == True:
            return Response(
                data={
                    "detail": "Эксперимент не одобрен",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            status=status.HTTP_200_OK
        )
