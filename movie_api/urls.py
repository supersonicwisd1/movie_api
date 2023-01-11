from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include('api_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
