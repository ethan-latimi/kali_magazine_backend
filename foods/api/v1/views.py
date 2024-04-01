# Django
from django.http import Http404
# DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Custom
from foods.models import FoodPost, FoodCategory
from foods.serializers import FoodCategorySerializer, FoodPostSerializer
from common.permissions import IsOwnerOrReadOnly



class FoodPostList(APIView):

    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        posts = FoodPost.objects.all()
        serializer = FoodPostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodPostDetail(APIView):

    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return FoodPost.objects.get(pk=pk)
        except FoodPost.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        FoodPost_obj = self.get_object(pk)
        serializer = FoodPostSerializer(FoodPost_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        FoodPost_obj = self.get_object(pk)
        serializer = FoodPostSerializer(FoodPost_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        FoodPost_obj = self.get_object(pk)
        FoodPost_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FoodCategoryList(APIView):

    def get(self, request):
        categories = FoodCategory.objects.all()
        serializer = FoodCategorySerializer(categories, many=True)
        return Response(serializer.data)