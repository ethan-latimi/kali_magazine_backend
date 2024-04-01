# Django
from django.http import Http404
# DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Custom
from businesses.models import BusinessPost, BusinessCategory
from businesses.serializers import BusinessCategorySerializer, BusinessPostSerializer
from common.permissions import IsOwnerOrReadOnly



class BusinessPostList(APIView):

    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        posts = BusinessPost.objects.all()
        serializer = BusinessPostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BusinessPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessPostDetail(APIView):

    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return BusinessPost.objects.get(pk=pk)
        except BusinessPost.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        BusinessPost_obj = self.get_object(pk)
        serializer = BusinessPostSerializer(BusinessPost_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        BusinessPost_obj = self.get_object(pk)
        serializer = BusinessPostSerializer(BusinessPost_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        BusinessPost_obj = self.get_object(pk)
        BusinessPost_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BusinessCategoryList(APIView):

    def get(self, request):
        categories = BusinessCategory.objects.all()
        serializer = BusinessCategorySerializer(categories, many=True)
        return Response(serializer.data)