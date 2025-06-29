from rest_framework import permissions


class IsParticipantOfConversation(permissions.BasePermission):

    """
    Allows only authenticated participants of the conversation to send (POST),
    view (GET), update (PUT/PATCH), or delete (DELETE).
    """

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user in obj.participants.all()
