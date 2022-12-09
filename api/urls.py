from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
   openapi.Info(
      title="Refbooks API",
      default_version='v1',
      description="Reference Book Register"
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('refbooks/', include('api.refbooks.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
