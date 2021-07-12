from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # *** if you want to use this in async context you cant access foreign-key related fields casually! ***
    def __str__(self):
        return str(self.pk)


class ChatMessage(models.Model):
    message = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    from_user = models.BooleanField(default=True)

    def __str__(self):
        return self.message


class SomeData(models.Model):
    num = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.num)