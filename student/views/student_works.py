from django.utils import timezone
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from clients.permissions import IsTeacherPermission, IsStudentPermission, IsAssistantPermission
from utils.paginations import SelectorPagination
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.student_works import StudentWork, StudentWorkReagents
from utils.serializers import MultiSerializerViewSet, ACTIONS
from ..serializers.student_works import BaseStudentWorkSerializer, \
    CreateStudentWorkSerializer, \
    BaseStudentByStudentWorkSerializer, ApprovedWorkSerializer


class TeacherStudentWorksModelViewSet(
    ModelViewSet,
    MultiSerializerViewSet
):
    queryset = StudentWork.objects.all()
    serializer_class = BaseStudentWorkSerializer
    serializers_class = {
        ACTIONS.LIST: BaseStudentWorkSerializer,
        ACTIONS.RETRIEVE: BaseStudentWorkSerializer,
        ACTIONS.POST: CreateStudentWorkSerializer,
        ACTIONS.PUT: CreateStudentWorkSerializer
    }
    permission_classes = [
        IsTeacherPermission
    ]
    pagination_class = SelectorPagination


class TodayStudentWorksModelViewSet(
    ReadOnlyModelViewSet
):
    queryset = StudentWork.objects.all()
    serializer_class = BaseStudentByStudentWorkSerializer
    permission_classes = [
        IsStudentPermission
    ]

    def get_queryset(self):
        return super().get_queryset().filter(
            student=self.request.user.client,
            date=timezone.now().date()
        )

    @action(methods=['POST'], detail=True, url_path='take')
    def take(self, request, *args, **kwargs):
        reagents = StudentWorkReagents.objects.filter(
            id=self.request.data.get('id')
        )
        if not reagents.exists():
            return Response(
                data={
                    "detail": "Реагент не найден",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        reagents = reagents.first()
        if request.data.get('real_quantity'):
            reagents.real_quantity = request.data.get('real_quantity')
            reagents.save()
        if not reagents.take():
            return Response(
                data={
                    "detail": "Реагент уже был взят или недостаточно реагента",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            status=status.HTTP_200_OK
        )


class LaboratoryDateWorksModelViewSet(
    ModelViewSet
):
    queryset = StudentWork.objects.all()
    serializer_class = ApprovedWorkSerializer
    permission_classes = [
        IsAssistantPermission
    ]
    pagination_class = SelectorPagination
