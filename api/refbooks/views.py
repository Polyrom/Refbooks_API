import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from api.refbooks.models import (ReferenceBook, ReferenceBookItem,
                                 ReferenceBookVersion)
from api.refbooks.serializers import (ReferenceBookSerializer,
                                      ReferenceBookItemSerializer)
from api.swagger_specs import parameters, response_schemas


class ReferenceBookView(GenericAPIView):
    """ Lists reference books by date is specified """
    serializer_class = ReferenceBookSerializer

    @swagger_auto_schema(manual_parameters=[parameters.date],
                         responses=response_schemas.list_refbooks)
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
            ).order_by('id').distinct()
        return queryset


class ReferenceBookItemsView(GenericAPIView):
    """ Lists reference book elements """
    serializer_class = ReferenceBookItemSerializer

    @swagger_auto_schema(manual_parameters=[parameters.version],
                         responses=response_schemas.list_elements)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'elements': serializer.data}, status=HTTP_200_OK)

    def get_queryset(self):
        """
        Filters reference book elements by book ID and version if specified.
        If version is not specified, returns the elements of the latest version.
        """
        refbooks = ReferenceBookItem.objects.all()
        version = self.request.query_params.get('version')
        current_version = ReferenceBookVersion.objects.filter(
            reference_book=self.kwargs['pk'],
            start_date__lte=datetime.date.today()).\
            order_by('-start_date').first().version
        if version is not None:
            current_version = version
        queryset = refbooks.filter(
            reference_book_version__reference_book=self.kwargs['pk'],
            reference_book_version__version=current_version
        )
        return queryset


class CheckElementView(APIView):
    """ Validates reference book element presence """

    @swagger_auto_schema(manual_parameters=[parameters.code,
                                            parameters.value,
                                            parameters.version],
                         responses=response_schemas.check_element)
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
            order_by('-start_date').first().version
        if version is not None:
            current_version = version
        return Response(refbook_items.filter(
            code=code, value=value,
            reference_book_version__version=current_version
        ).exists())
