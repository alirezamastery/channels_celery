from django.contrib import admin

from .models import ChatMessage, Chat,SomeData


class ChatAdmin(admin.ModelAdmin):
    class Media:
        css = {'all': ('admin/css/chat.css',)}

    readonly_fields = ('user',)
    save_as = False
    save_on_top = False
    save_as_continue = False

    def has_add_permission(self, request):
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        user_obj = Chat.objects.get(id=object_id).user
        context = {
            'user_obj': user_obj
        }
        return super().change_view(request, object_id, form_url='', extra_context=context)


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'from_user']


admin.site.register(Chat, ChatAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)
admin.site.register(SomeData)
