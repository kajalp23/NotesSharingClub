
from django.contrib import admin
from onlinenotes.models import signup,notes,Message,Room,notification,creatednotes,contactus
# Register your models here.

class creatednotesAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'title', 'description']

admin.site.register(signup)
admin.site.register(notes)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(notification)
admin.site.register(contactus)
admin.site.register(creatednotes,creatednotesAdmin)