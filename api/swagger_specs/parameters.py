from drf_yasg import openapi

# Parameters definitions for Swagger UI

date = openapi.Parameter('date', openapi.IN_QUERY,
                         description='Specify date to see active '
                                     'reference books for the date',
                         type=openapi.TYPE_STRING,
                         format=openapi.FORMAT_DATE,
                         required=False)

version = openapi.Parameter('version', openapi.IN_QUERY,
                            description='Reference book version',
                            type=openapi.TYPE_STRING,
                            required=False)

code = openapi.Parameter('code', openapi.IN_QUERY,
                         description='Element code',
                         type=openapi.TYPE_STRING,
                         required=True)

value = openapi.Parameter('value', openapi.IN_QUERY,
                          description='Element value',
                          type=openapi.TYPE_STRING,
                          required=True)
