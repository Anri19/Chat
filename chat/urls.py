
# chat/urls.py
from django.urls import path
 
from .views import MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView # новое изменение
 
urlpatterns = [
    path('post/<int:pk>/delete/', # Создаем новый маршрут
    MessageDeleteView.as_view(), name='message_delete'),
    path('message/<int:pk>/edit/',
    MessageUpdateView.as_view(), name='message_edit'), # Новый маршрут
	path('message/new/', MessageCreateView.as_view(), name='message_new'), # new
	path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'), # новое изменение
    path('', MessageListView.as_view(), name='home'),
]

#path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'), # новое изменение