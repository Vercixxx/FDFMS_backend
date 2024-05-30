from rest_framework import serializers

from users.models import GeneralUser
from .models import MyMessages

class GetMessagesSerializer(serializers.ModelSerializer):
        
    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()
    
    posted_date = serializers.DateTimeField(format='%Y-%m-%d')

    def get_sender(self, obj):
        user_id = obj.sender.id
        try:
            user = GeneralUser.objects.get(id=user_id)
            return user.username
        except GeneralUser.DoesNotExist:
            return None

    def get_receiver(self, obj):
        user_id = obj.receiver.id
        try:
            user = GeneralUser.objects.get(id=user_id)
            return user.username
        except GeneralUser.DoesNotExist:
            return None
        
        
    class Meta:
        model = MyMessages
        fields = '__all__'
        
        
class CreateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyMessages
        fields = ['sender', 'receiver', 'title', 'content']
    
    def create(self, validated_data):
        post = MyMessages.objects.create(**validated_data)
        return post