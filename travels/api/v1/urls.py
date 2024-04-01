from django.urls import path
from .views import TravelCategoryList, TravelPostList, TravelPostDetail

urlpatterns = [
    path('', TravelPostList.as_view()),
    path('<int:pk>', TravelPostDetail.as_view()),
    path('categories', TravelCategoryList.as_view()),
]