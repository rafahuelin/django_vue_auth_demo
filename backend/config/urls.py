from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('reports.urls')),
    path('api/v1/user/', include('users.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/api-token-auth/', obtain_jwt_token),
    path('api/v1/api-token-refresh/', refresh_jwt_token),
] + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
