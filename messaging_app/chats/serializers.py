
from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["email", "first_name",
                  "last_name", "phone_number", "full_name"]
        read_only_fields = ['email']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at']
        read_only_fields = ['message_id', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    title = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants',
                  'created_at', 'messages', 'title']
        read_only_fields = ['conversation_id']

    def validate_title(self, value):
        if "badword" in value.lower():
            raise serializers.ValidationError(
                "Title contains inappropriate content.")
        return value
