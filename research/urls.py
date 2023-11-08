from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.research import ResearchModelViewSet
from .views.work_request import WorkRequestStudentModelViewSet, WorkRequestTeacherModelViewSet, WorkRequestTeacherApprovedModelViewSet

research_router = SimpleRouter()
work_request_router = SimpleRouter()

research_router.register(prefix='researches', viewset=ResearchModelViewSet, basename='research')
work_request_router.register(prefix='work_requests', viewset=WorkRequestStudentModelViewSet, basename='student|work_requests')
work_request_router.register(prefix='work_requests', viewset=WorkRequestTeacherModelViewSet, basename='teacher|work_requests')
work_request_router.register(prefix='work_requests', viewset=WorkRequestTeacherApprovedModelViewSet, basename='teacher|work_requests|approved')

urlpatterns = [
    path('', include(research_router.urls)),
    path('', include(work_request_router.urls))
]
