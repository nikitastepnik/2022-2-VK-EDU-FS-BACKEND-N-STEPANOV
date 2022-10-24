from django.db import models

from chat_api.models import User, Chats


class Messages(models.Model):
    content = models.TextField("Содержимое сообщения", blank=True)
    dispatch_date = models.DateTimeField("Дата отправки", auto_now_add=True)
    author = models.ForeignKey(User, verbose_name="Автор сообщения", on_delete=models.SET_NULL,
                               null=True, related_name="author_of_msgs")
    chat_id = models.ForeignKey(Chats, verbose_name="Идентификатор чата", on_delete=models.SET_NULL,
                                null=True, related_name="messages_in_chat")

    def __str__(self):
        return f"{self.author} {self.dispatch_date}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
