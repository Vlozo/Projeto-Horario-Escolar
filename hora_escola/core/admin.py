from django.contrib import admin
from .models import Client, Room_Class

class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'room_class', 'student_id')
    list_filter = ('room_class', 'type')
    search_fields = ('student_id', 'user')

class Room_ClassAdmin(admin.ModelAdmin):
    list_display = ("room_class",)
    
admin.site.register(Client, ClientAdmin)
admin.site.register(Room_Class, Room_ClassAdmin)


