from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:room_name>/', room, name='room'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
