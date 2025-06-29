from rest_framework import routers
from django.urls import path, include
from chats import views


router = routers.DefaultRouter()

router.register(r"Conversations", views.ConversationViewSet,
                basename='conversation')


urlpatterns = [
    path("", include(router.urls)),
    path('conversations/<int:conversation_id>/messages/',
         views.MessageViewSet.as_view({...})),
]
