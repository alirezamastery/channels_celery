from django.shortcuts import render
from django.http import JsonResponse

from .models import ChatMessage
from .forms import ChatMessageForm


def index_view(request):
    return render(request, 'chat/chat.html')


def save_chat_msg_view(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            message = form.cleaned_data.get('message', None)
            if message:
                ChatMessage.objects.create(message=message, user=request.user)
                return JsonResponse({'info': 'message saved'}, status=200)
    return JsonResponse({}, status=400)