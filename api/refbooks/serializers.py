from rest_framework import serializers
from api.refbooks.models import (ReferenceBook,
                                 ReferenceBookVersion,
                                 ReferenceBookItem)


class ReferenceBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReferenceBook
        fields = ['id', 'code', 'name']


class ReferenceBookVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReferenceBookVersion
        fields = '__all__'


class ReferenceBookItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReferenceBookItem
        fields = ['code', 'value']
