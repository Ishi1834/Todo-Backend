from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    # hides the author field, therefore it is set automatically to the current logged in user
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # changes the category value from the id to the name but cant post with it
    # category = serializers.CharField(source='category.name', allow_null=True)
    class Meta:
        fields = ('id','author', 'title', 'body','done','category' , 'created_at','updated_at',)
        model = Todo

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id',  'email', 'username', 'first_name', 'last_name')

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username',)