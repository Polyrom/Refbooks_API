from rest_framework import serializers
from api.refbooks.models import (ReferenceBook,
                                 ReferenceBookVersion,
                                 ReferenceBookElement)


class ReferenceBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReferenceBook
        fields = ['id', 'code', 'name']


class ReferenceBookVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReferenceBookVersion
        fields = '__all__'


class ReferenceBookElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReferenceBookElement
        fields = ['code', 'value']
