from django.contrib import admin
from django.urls import path, include

from api.swagger_specs.view_schema import schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('refbooks/', include('api.refbooks.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs')
]
