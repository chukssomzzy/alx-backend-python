from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from django_filters import rest_framework as filters
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import MessageSerializer, ConversationSerializer
from .permissions import IsParticipantOfConversation
from .pagination import StandardResultsSetPagination
from .filters import MessageFilter


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at']
    search_fields = ['participants_first_email']

    permission_classes = [permissions.IsAuthenticated,
                          IsParticipantOfConversation]


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    filter_backends = (filters.DjangoFilterBackend)
    filterset_class = MessageFilter

    permission_classes = [permissions.IsAuthenticated]

    pagination_class = [StandardResultsSetPagination]

    def get_queryset(self):

        conversation_id = self.kwargs.get('conversation_id')

        if conversation_id:
            return Message.objects.filter(conversation_id)
        return Response(data={"Error": "Missing Converstion ID"}, status=status.HTTP_403_FORBIDDEN)
