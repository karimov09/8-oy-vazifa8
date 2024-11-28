from django.urls import path
from .views import (FoodTypeListCreateView, FoodTypeDetailView, FoodListCreateView, FoodDetailView, CommentListCreateView, CommentDetailView, RegisterView, LoginView, LogoutView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('foodtypes/', FoodTypeListCreateView.as_view(), name='foodtype-list-create'),
    path('foodtypes/<int:pk>/', FoodTypeDetailView.as_view(), name='foodtype-detail'),
    path('foods/', FoodListCreateView.as_view(), name='food-list-create'),
    path('foods/<int:pk>/', FoodDetailView.as_view(), name='food-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
