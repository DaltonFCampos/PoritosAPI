from os import path
from rest_framework.routers import DefaultRouter

from animal.api.viewset.animal_viewset import AnimalViewSet

router = DefaultRouter()
router.register(r'animais', AnimalViewSet, basename='animal')
urlpatterns = router.urls

router.register(r'listar_animais_usuario', AnimalViewSet, basename='listar_animais_usuario')