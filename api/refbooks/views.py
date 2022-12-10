import datetime

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from api.refbooks.models import (ReferenceBook, ReferenceBookItem,
                                 ReferenceBookVersion)
from api.refbooks.serializers import (ReferenceBookSerializer,
                                      ReferenceBookItemSerializer)


class ReferenceBookView(ListAPIView):
    """ Lists reference books """
    serializer_class = ReferenceBookSerializer

    date = openapi.Parameter('date', openapi.IN_QUERY,
                             description='Active refbooks for the date',
                             type=openapi.FORMAT_DATE)

    @swagger_auto_schema(manual_parameters=[date])
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'refbooks': serializer.data}, status=HTTP_200_OK)

    def get_queryset(self):
        """ Filters reference books by date if specified """
        queryset = ReferenceBook.objects.all()
        date = self.request.query_params.get('date')
        if date is not None:
            queryset = queryset.filter(
                referencebookversion__start_date__lte=date
            )
        return queryset


class ReferenceBookItemsView(ListAPIView):
    """ Lists reference book elements """
    serializer_class = ReferenceBookItemSerializer

    version = openapi.Parameter('version', openapi.IN_QUERY,
                                description='Refbook version',
                                type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[version],
                         operation_description='Filters reference book '
                                               'elements by book ID '
                                               'and version if specified. '
                                               'If version is not specified, '
                                               'returns the elements of '
                                               'the latest version.')
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'elements': serializer.data}, status=HTTP_200_OK)

    def get_queryset(self):
        """
        Filters reference book elements by book ID and version if specified.
        If version is not specified, returns the elements of the latest version.
        """
        queryset = ReferenceBookItem.objects.all()
        version = self.request.query_params.get('version')
        current_version = ReferenceBookVersion.objects.filter(
            reference_book=self.kwargs['pk'],
            start_date__lte=datetime.date.today()).\
            order_by('-start_date').first()
        if version is not None:
            current_version = version
        queryset = queryset.filter(
            reference_book_version__reference_book=self.kwargs['pk'],
            reference_book_version__version=current_version
        )
        return queryset


class CheckElementView(APIView):
    """ Validates reference book element presence """

    code = openapi.Parameter('code', openapi.IN_QUERY,
                             description='Element code',
                             type=openapi.TYPE_STRING,
                             required=True)
    value = openapi.Parameter('value', openapi.IN_QUERY,
                              description='Element value',
                              type=openapi.TYPE_STRING,
                              required=True)
    version = openapi.Parameter('version', openapi.IN_QUERY,
                                description='Refbook version',
                                type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[code, value, version])
    def get(self, request, **kwargs):
        """
        Checks reference book element existence by code,
        value and reference book version if specified.
        If version is not specified, checks among the elements
        of the latest version.
        """
        refbook_items = ReferenceBookItem.objects.filter(
            reference_book_version__reference_book=kwargs['pk']
        ).all()
        code = self.request.query_params.get('code')
        value = self.request.query_params.get('value')
        version = self.request.query_params.get('version')
        current_version = ReferenceBookVersion.objects.filter(
            reference_book=kwargs['pk'],
            start_date__lte=datetime.date.today()).\
            order_by('-start_date').first()
        if version is not None:
            current_version = version
        return Response(refbook_items.filter(
            code=code, value=value,
            reference_book_version__version=current_version
        ).exists())
