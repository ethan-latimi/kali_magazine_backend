from django.urls import path
from .views import BusinessCategoryList, BusinessPostList, BusinessPostDetail

urlpatterns = [
    path('', BusinessPostList.as_view()),
    path('<int:pk>', BusinessPostDetail.as_view()),
    path('categories', BusinessCategoryList.as_view()),
]