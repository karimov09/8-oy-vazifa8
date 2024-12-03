from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodTypeViewSet, FoodViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'foodtypes', FoodTypeViewSet, basename='foodtype')
router.register(r'foods', FoodViewSet, basename='food')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls

