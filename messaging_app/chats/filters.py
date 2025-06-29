from django_filters import rest_framework as filters
from .models import Message


class MessageFilter(filters.FilterSet):

    class Meta:
        model = Message
        fields = ["users", "sent_at"]
