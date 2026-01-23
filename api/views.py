from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from api.serializators import LotSerializer
from lots.models import Lot

# Create your views here.

class LotsList(APIView):

    @action(method=['get'], detail=False)
    def get(self, request, format=None):
        lots = Lot.objects.all()
        serializer = LotSerializer(lots, many=True)
        return Response(serializer.data)
    
    @action(method=['post'], detail=False)
    def post(self, request, format=None):
        serializer = LotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LotsDetail(APIView):
    @action(method=['get'], detail=False)
    def get(self, request, pk, format=None):
        lot = self.get_object(pk)
        serializer = LotSerializer(lot)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Lot.objects.get(pk=pk)
        except Lot.DoesNotExist:
            return Http404

    @action(methods=['put'], detail=False)
    def put(self, request, pk, format=None):
        lot = self.get_object(pk)
        serializer = LotSerializer(lot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(method=['delete'], detail=False)
    def delete(self, request, pk, format=None):
        lot = self.get_object(pk)
        lot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)