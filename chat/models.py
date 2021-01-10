from django.db import models
from django.urls import reverse # Новый импорт

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
 
    def __str__(self):
        return self.title

    def get_absolute_url(self): # Тут мы создали новый метод
    	return reverse('message_detail', args=[str(self.id)])