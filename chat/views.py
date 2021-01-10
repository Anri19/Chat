from django.shortcuts import render

# Create your views here.

# chat/views.py
from django.views.generic import ListView, DetailView # новое 

from django.views.generic.edit import CreateView, UpdateView, DeleteView # новое изменение

from django.urls import reverse_lazy # импортируем новые методы
 
from .models import Message
 
 
class MessageListView(ListView):
    model = Message
    template_name = 'home.html'

class MessageDetailView(DetailView): # новое
    model = Message
    template_name = 'message_detail.html'

class MessageCreateView(CreateView): # новое изменение
	model = Message
	template_name = 'message_new.html'
#	model.author = User.Username # request.user
 #   fields = ['title', 'author'= 'request.user', 'body']
	fields = ['title', 'author', 'body']

class MessageUpdateView(UpdateView): # Новый класс
    model = Message
    template_name = 'message_edit.html'
    fields = ['title', 'body']

class MessageDeleteView(DeleteView): # Создание нового класса
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('home')