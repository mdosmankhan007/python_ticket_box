from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.hashers import make_password
# Create your models here.


role=(('OILC_Manager','OILC_Manager'),('Deployed_Manager','Deployed_Manager'),('Employee','Employee'),('admin','admin'))
class Pusers(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role=models.CharField(max_length=100,choices=role)
    def __str__(self):
        return self.username

severity=(('high','high'),('medium','medium'),('low','low'))
status=(('raised','raised'),('accepted','accepted'),('rejected','rejected'),('complete','complete'))
type=(('hardware','hardware'),('software','software'),('cubical','cubical'),('conference room','conference room'),('stationary','stationary'),('other','other'))
manager=(('OILC_Manager','OILC_Manager'),('Deployed_Manager','Deployed_Manager'))
class Ticket(models.Model):
    ticket_no=models.CharField(max_length=20,unique=True,default='OJ-'+'')
    user=models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    Subject=models.CharField(max_length=100)
    Severity=models.CharField(max_length=100,choices=severity)
    Type=models.CharField(max_length=100,choices=type)
    Report_To=models.CharField(max_length=100,choices=manager)
    Remarks=models.TextField()
    Status=models.CharField(max_length=100,choices=status,default='raised')
    Admin_comment=models.CharField(max_length=100,default='')
    Mgr_comment = models.CharField(max_length=100,default='')
    request_raised_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user)

class RoleAPI(models.Model):
    role=models.CharField(max_length=100)

    def __str__(self):
        return str(self.role)

class UsersAPI(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.ForeignKey(RoleAPI,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.username

class SeverityAPI(models.Model):
    severity=models.CharField(max_length=100)

    def __str__(self):
        return str(self.severity)

class StatusAPI(models.Model):
    status=models.CharField(max_length=100)

    def __str__(self):
        return str(self.status)

class TypeAPI(models.Model):
    type=models.CharField(max_length=100)

    def __str__(self):
        return str(self.type)

class ManagerAPI(models.Model):
    manager=models.CharField(max_length=100)

    def __str__(self):
        return str(self.manager)


class TicketAPI(models.Model):
    ticket_no=models.CharField(max_length=20,unique=True)
    user=models.CharField(max_length=30,default="")
    Subject=models.CharField(max_length=100)
    Severity=models.ForeignKey(SeverityAPI,on_delete=models.CASCADE)
    Type=models.ForeignKey(TypeAPI,on_delete=models.CASCADE)
    Report_To=models.ForeignKey(ManagerAPI,on_delete=models.CASCADE)
    Remarks=models.TextField()
    Status=models.ForeignKey(StatusAPI,on_delete=models.CASCADE, default=1)
    Admin_comment=models.CharField(max_length=100,default='')
    Mgr_comment = models.CharField(max_length=100,default='')
    request_raised_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.ticket_no)
