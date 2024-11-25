from rest_framework.generics import GenericAPIView
from rest_framework import mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import FoodType, Food, Comment
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer


class FoodTypeView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Get all FoodType objects.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create a new FoodType.
        """
        return self.create(request, *args, **kwargs)


class FoodView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Get all Food objects.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create a new Food.
        """
        return self.create(request, *args, **kwargs)


class CommentView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Get all Comment objects.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create a new Comment.
        """
        return self.create(request, *args, **kwargs)


class RegisterView(APIView):
    """
    Register a new user.
    """
    def post(self, request):
        data = request.data
        try:
            user = User.objects.create(
                username=data['username'],
                password=make_password(data['password'])
            )
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
