from django.urls import path
from .views import FoodCategoryList, FoodPostList, FoodPostDetail

urlpatterns = [
    path('', FoodPostList.as_view()),
    path('<int:pk>', FoodPostDetail.as_view()),
    path('categories', FoodCategoryList.as_view()),
]