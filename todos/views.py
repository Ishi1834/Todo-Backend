from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import Todo
from .permissions import IsAuthorOrNothing
from .serializers import TodoSerializer, UserSerializer, UserListSerializer


class TodoList(generics.ListCreateAPIView):

    model = Todo
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        queryset = self.model.objects.filter(author = self.request.user)
        return queryset


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrNothing,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserListSerializer

class UserProfile(generics.ListAPIView):
    model = get_user_model()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = self.model.objects.filter(username = self.request.user)
        return queryset
