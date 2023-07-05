from rest_framework import routers
from .api import CitaViewSet

# Crear crud con el routers
router = routers.DefaultRouter()

router.register('api/cita', CitaViewSet, 'cita')

urlpatterns = router.urls
