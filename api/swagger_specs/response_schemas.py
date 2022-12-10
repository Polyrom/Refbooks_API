from drf_yasg import openapi

from api.refbooks.serializers import (ReferenceBookSerializer,
                                      ReferenceBookItemSerializer)

# Example responses for Swagger UI
list_refbooks = {
    "200": openapi.Response(
        description="Success",
        schema=ReferenceBookSerializer,
        examples={
            "application/json": {
                "refbooks": [
                    {
                        "id": 1,
                        "code": "MS-1",
                        "name": "MS-1 name"
                    },
                    {
                        "id": 2,
                        "code": "ICD-10",
                        "name": "ICD-10 name"
                    }
                ]
            }
        }
    ),
}

list_elements = {
    "200": openapi.Response(
        description="Success",
        schema=ReferenceBookItemSerializer,
        examples={
            "application/json": {
                "elements": [
                    {
                        "code": "J00",
                        "value": "J00 value"
                    },
                    {
                        "code": "J01",
                        "value": "J01 value"
                    }
                ]
            }
        }
    )
}

check_element = {
    "200": openapi.Response(
        description="Success",
        examples={
            "application/json": "true"
        }
    )
}
