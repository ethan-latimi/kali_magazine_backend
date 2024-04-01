# Django
from django.http import Http404
# DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Custom
from travels.models import TravelPost, TravelCategory
from travels.serializers import TravelCategorySerializer, TravelPostSerializer
from common.permissions import IsOwnerOrReadOnly



class TravelPostList(APIView):

    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        posts = TravelPost.objects.all()
        serializer = TravelPostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TravelPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TravelPostDetail(APIView):

    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return TravelPost.objects.get(pk=pk)
        except TravelPost.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        TravelPost_obj = self.get_object(pk)
        serializer = TravelPostSerializer(TravelPost_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        TravelPost_obj = self.get_object(pk)
        serializer = TravelPostSerializer(TravelPost_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        TravelPost_obj = self.get_object(pk)
        TravelPost_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TravelCategoryList(APIView):

    def get(self, request):
        categories = TravelCategory.objects.all()
        serializer = TravelCategorySerializer(categories, many=True)
        return Response(serializer.data)