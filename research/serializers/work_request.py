from rest_framework.serializers import ModelSerializer
from inventory.models import Work
from ..models import WorkRequest
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class BaseWorkRequestTeacherSerializer(ModelSerializer):

    class Meta:
        model = WorkRequest
        fields = 'all'

class BaseWorkRequestStudentSerializer(ModelSerializer):

    class Meta:
        model = WorkRequest
        exclude = ("work")
        is_approved = serializers.BooleanField(is_approved=False)
    def validate(self, attrs):
        if not attrs.get('student').is_student:
            raise ValidationError(
                detail={
                    'detail': 'Пользователь не является студентом'
                }
            )
        return attrs

class BaseWorkRequestApprovedSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = 'all'
    def validate(self, attrs):
        if not attrs.get('teacher').is_teacher:
            raise ValidationError(
                detail={
                    'detail': 'Пользователь не является преподавателем'
                }
            )
        return attrs