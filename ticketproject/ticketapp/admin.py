from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=['id','user','ticket_no','Subject','Severity','Type','Report_To','Remarks','request_raised_at','Status','Admin_comment','Mgr_comment']

@admin.register(Pusers)
class PuserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','role','email']

@admin.register(UsersAPI)
class UserAPIAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','role','email']

@admin.register(SeverityAPI)
class UserAPIAdmin(admin.ModelAdmin):
    list_display = ['severity']

@admin.register(StatusAPI)
class UserAPIAdmin(admin.ModelAdmin):
    list_display = ['status']

@admin.register(TypeAPI)
class UserAPIAdmin(admin.ModelAdmin):
    list_display = ['type']

@admin.register(ManagerAPI)
class UserAPIAdmin(admin.ModelAdmin):
    list_display = ['manager']

@admin.register(TicketAPI)
class TicketAPIAdmin(admin.ModelAdmin):
    list_display = ['id','ticket_no','Subject','Severity','Type','Report_To','Remarks','request_raised_at','Status','Admin_comment','Mgr_comment']

