from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
from .models import Info, Info2
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InfoSerializer, Info2Serializer

class InfoList(APIView):
    @api_view(['POST'])
    def post(self,request):
        now_info = Info.object.get(id=id)
        serializer = InfoSerializer(now_info)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    @api_view(['GET'])
    def get(self,request):
        queryset = Info.objects.all()
        serializer = InfoSerializer(queryset, many=True)
        return Response(serializer.data)

class InfoDetail(APIView) :
    def get_object(self,request):
        try :
            return Info.objects.get(id=id)
        except :
            raise Http404
    @api_view(['GET'])
    def get(self,request):
        now_info = Info.object.get(id=id)
        serializer = InfoSerializer(now_info)
        return Response(serializer.data)
    @api_view(['PUT'])
    def put(self,request):
        now_info = Info.object.get(id=id)
        serializer = InfoSerializer(now_info)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    @api_view(['DELETE'])
    def delete(self,request):
        now_info = Info.object.get(id=id)
        now_info.delete()
        return Response("Clear")



    