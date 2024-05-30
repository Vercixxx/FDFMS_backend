from rest_framework import serializers
from .models import Posts, DriverPosts
from users.models import GeneralUser

class GetPostsSerializer(serializers.ModelSerializer):
    posted_date = serializers.DateTimeField(format='%Y-%m-%d')
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ['id', 'posted_date', 'author_username', 'title', 'content']

    def get_author_username(self, obj):
        user = obj.author
        try:
            user = GeneralUser.objects.get(username=user)
            return user.username
        except GeneralUser.DoesNotExist:
            return None
        
        
class GetDriverPostsSerializer(serializers.ModelSerializer):
    posted_date = serializers.DateTimeField(format='%Y-%m-%d')
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = DriverPosts
        fields = ['id', 'posted_date', 'author_username', 'title', 'content']

    def get_author_username(self, obj):
        user = obj.author.pk
        try:
            user = GeneralUser.objects.get(username=user)
            return user.username
        except GeneralUser.DoesNotExist:
            return None
        
        

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['author', 'title', 'content']
                
    
    def create(self, validated_data):
        post = Posts.objects.create(**validated_data)
        return post
    
    
class CreateDriverPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverPosts
        fields = ['author', 'title', 'content']
    
    def create(self, validated_data):
        post = DriverPosts.objects.create(**validated_data)
        return post