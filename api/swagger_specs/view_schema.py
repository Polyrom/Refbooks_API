from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# View schema definition for Swagger UI

schema_view = get_schema_view(
    openapi.Info(
        title="Reference Books",
        default_version='1.0.0',
        description="Test API project for handling reference books."
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
