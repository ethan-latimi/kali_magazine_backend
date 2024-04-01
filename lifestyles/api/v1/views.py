# Django
from django.http import Http404
# DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Custom
from lifestyles.models import LifestylePost, LifestyleCategory
from lifestyles.serializers import LifestyleCategorySerializer, LifestylePostSerializer
from common.permissions import IsOwnerOrReadOnly



class LifestylePostList(APIView):

    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        posts = LifestylePost.objects.all()
        serializer = LifestylePostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LifestylePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LifestylePostDetail(APIView):

    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return LifestylePost.objects.get(pk=pk)
        except LifestylePost.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        LifestylePost_obj = self.get_object(pk)
        serializer = LifestylePostSerializer(LifestylePost_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        LifestylePost_obj = self.get_object(pk)
        serializer = LifestylePostSerializer(LifestylePost_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        LifestylePost_obj = self.get_object(pk)
        LifestylePost_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LifestyleCategoryList(APIView):

    def get(self, request):
        categories = LifestyleCategory.objects.all()
        serializer = LifestyleCategorySerializer(categories, many=True)
        return Response(serializer.data)