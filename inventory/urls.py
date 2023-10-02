from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.reagents import ReagentsModelViewSet, WorkReagentsModelViewSet, UnitsTypeView
from .views.works import WorksModelViewSet
from .views.equipment import EquipmentModelViewSet

inventory_router = SimpleRouter()
inventory_router.register(prefix='reagents', viewset=ReagentsModelViewSet, basename='reagents')
inventory_router.register(prefix='works', viewset=WorksModelViewSet, basename='works')

work_reagents_router = SimpleRouter()
work_reagents_router.register(prefix='reagents', viewset=WorkReagentsModelViewSet, basename='work|reagents')

equipment_router = SimpleRouter()
equipment_router.register(prefix='equipments',viewset=EquipmentModelViewSet, basename='equipments')

urlpatterns = [
    path('', include(inventory_router.urls)),
    path('works/<int:work_id>/', include(work_reagents_router.urls)),
    path('units/type/', view=UnitsTypeView.as_view(), name='units|type'),
    path('', include(equipment_router.urls))
]
