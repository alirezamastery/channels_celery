from django.urls import path

from .views import *


urlpatterns = [
    path('', index_view, name='online-chat'),
    path('save-message/', save_chat_msg_view, name='save-message'),
]