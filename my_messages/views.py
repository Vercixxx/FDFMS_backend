from django.http import JsonResponse

from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .models import MyMessages
from users.models import GeneralUser

from .serializers import GetMessagesSerializer, CreateMessageSerializer

from users.views import GlobalDictionaries


class GetMessages(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = self.request.query_params.get('query', '').strip()
        mail_version = self.request.query_params.get('version', '').strip()
        username = self.request.query_params.get('user', '').strip()

        try:
            user = GeneralUser.objects.get(username=username)
        
            if mail_version == 'all':
                all_messages = MyMessages.objects.filter(Q(receiver=user) | Q(sender=user)).order_by('-posted_date')
                
            else:
                if mail_version == 'inbox':
                    all_messages = MyMessages.objects.filter(receiver=user).order_by('-posted_date')
                else:
                    all_messages = MyMessages.objects.filter(sender=user).order_by('-posted_date')
                    
        except GeneralUser.DoesNotExist as error:
            return JsonResponse((''), status=404, safe=False)
        
                    
        if query:
            all_messages = [message for message in all_messages if
                     query.lower() in message.sender.username.lower() or
                     query.lower() in message.receiver.username.lower() or
                     query.lower() in message.title.lower() or
                     query.lower() in message.content.lower()]
        
        serialized_data = GetMessagesSerializer(all_messages, many=True)

        return JsonResponse(serialized_data.data, safe=False)
    
    
    
    
class CreateMessage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        
        if data.get('taget') == 'Users':
            targets = data.get('to')
            title = data.get('title')
            content = data.get('content')
            sender = GeneralUser.objects.get(username=data.get('from')).pk

            for receiver in targets:

                receiver = GeneralUser.objects.get(username=receiver).pk

                user_data = {
                    'title': title,
                    'content': content,
                    'sender': sender,
                    'receiver': receiver,
                }

                serializer = CreateMessageSerializer(data=user_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return JsonResponse({'errors': serializer.errors}, status=400)

            return JsonResponse({'message': 'Messages sent successfully'}, status=201)
        else:
            groups = data.get('to')
            title = data.get('title')
            content = data.get('content')
            sender = GeneralUser.objects.get(username=data.get('from')).pk
            
            for group in groups:
                user_model = GlobalDictionaries.get_serializer('UserModels', group)

                users = user_model.objects.all()

                for user in users:
                    user_data = {
                        'title': title,
                        'content': content,
                        'sender': sender,
                        'receiver': user_model.objects.get(username=user.username).pk,
                    }

                    serializer = CreateMessageSerializer(data=user_data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return JsonResponse({'errors': serializer.errors}, status=400)
                    
            return JsonResponse({'message': 'Messages sent successfully'}, status=201)
        

        
        


    
# Delete 
class DeleteMessages(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        message_ids = request.data.get('message_ids', [])
        for message_id in message_ids:
            message = MyMessages.objects.get(id=message_id)
            message.delete()
        return JsonResponse({'message': 'Messages deleted successfully'}, status=200)
# Delete 