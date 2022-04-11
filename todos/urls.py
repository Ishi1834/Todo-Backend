from django.urls import path
from .views import TodoList, TodoDetail, UserProfile,  UserList


urlpatterns = [
    path('', TodoList.as_view()),
    path('<int:pk>/', TodoDetail.as_view()),
    path('users/', UserList.as_view()),
    path('user/', UserProfile.as_view()),
]
