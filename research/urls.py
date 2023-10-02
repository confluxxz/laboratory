from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.research import ResearchModelViewSet
from .views.work_request import WorkRequestModelViewSet

research_router = SimpleRouter()
work_request_router = SimpleRouter()
research_router.register(prefix='researches', viewset=ResearchModelViewSet, basename='research')
work_request_router.register(prefix='work_requests', viewset=WorkRequestModelViewSet, basename='work_requests')

urlpatterns = [
    path('', include(research_router.urls)),
    path('', include(work_request_router.urls)),
]
