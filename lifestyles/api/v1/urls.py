from django.urls import path
from .views import LifestyleCategoryList, LifestylePostList, LifestylePostDetail

urlpatterns = [
    path('', LifestylePostList.as_view()),
    path('<int:pk>/', LifestylePostDetail.as_view()),
    path('categories', LifestyleCategoryList.as_view()),
]