from rest_framework import serializers
from posts.models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer
from tipo.api.serializers import TipoSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    tipo = TipoSerializer()

    class Meta:
        model = Post
        fields = ['title', 'miniature', 'created_at', 'published', 'user', 'category', 'tipo']
