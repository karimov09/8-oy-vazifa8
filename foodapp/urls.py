from django.urls import path
from .views import FoodTypeView, FoodView, CommentView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('foodtypes/', FoodTypeView.as_view(), name='foodtype-list'),
    path('foods/', FoodView.as_view(), name='food-list'),
    path('comments/', CommentView.as_view(), name='comment-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]



