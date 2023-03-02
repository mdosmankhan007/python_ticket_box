from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
import uuid
import datetime
from django.views.decorators.csrf import csrf_exempt

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField()
    class Meta:
        model = UsersAPI
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'role']
        extra_kwargs={
            'password':{'write_only':True}
        }
    # print('outside def')
    def create(self, validated_data):
            print(validated_data,'validated data')
            request = self.context.get('request')
            password = validated_data.pop('password')
            print(password)
            role = request.data.get('role')
            print(role)
            role = RoleAPI.objects.get(role=role)
            print(role)
            print(validated_data['role'],"-----------------------------------jsdjkvsjkdvbsjkv")
            validated_data['role'] = role

            instance = self.Meta.model(**validated_data)
            # role = request.data['role']
            print(role, 'input')

            instance.role = role
            instance.save()
            print(instance,"-------------------------------------")
            user = User.objects.create(
                username=validated_data['username'])
            user.set_password(password)
            if role.role=='admin':
                user.is_superuser=True
                user.is_staff=True
                user.save()
                print(user.is_superuser)
            elif role.role == 'manager':
                    user.is_staff=True
                    user.save()
            # elif role.role == 'Deployed_Manager':
            #         user.is_superuser = True
            #         user.save()
            else:
                    user.save()
            print('outside..............')
            # instance1.save()
            return instance


class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
       


class RoleAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleAPI
        fields = ['role']


class SeverityAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = SeverityAPI
        fields = ['id', 'severity']

class StatusAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusAPI
        fields = ['id', 'status']

class TypeAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAPI
        fields = ['id', 'type']

class ManagerAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = ManagerAPI
        fields = ['id', 'manager']



# class TicketSerializer(serializers.ModelSerializer):
#     Severity = serializers.CharField(source='Severity.severity', read_only=True)
#     Report_To = serializers.CharField(source='Report_To.manager', read_only=True)
#     Type = serializers.CharField(source='Type.type', read_only=True)
#     Status = serializers.CharField(source='Status.status', read_only=True)
#     ticket_no = serializers.CharField(required=False)
#     user = serializers.CharField()
#     class Meta:
#         model = TicketAPI
        
#         fields = [ 'ticket_no','user', 'Subject', 'Severity', 'Type', 'Report_To', 'Remarks', 'Status', 'Admin_comment',
#                    'Mgr_comment', 'request_raised_at']
    
    
    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     ticket_no = "OJ-"+uuid.uuid4().hex[:6]
    #     validated_data['ticket_no'] = ticket_no
        
    #     Severity = request.data.get('Severity')
    #     Severity = SeverityAPI.objects.get(severity=Severity)
    #     validated_data['Severity'] = Severity

    #     Report_To = request.data.get('Report_To')
    #     Report_To = ManagerAPI.objects.get(manager=Report_To)
    #     validated_data['Report_To'] = Report_To

    #     Type = request.data.get('Type')
    #     Type = TypeAPI.objects.get(type=Type)
    #     validated_data['Type'] = Type
        
    #     user=request.user.username
        
    #     validated_data['user']=user
        
        
    #     instance = self.Meta.model(**validated_data)
    #     instance.user=user
    #     instance.Severity = Severity
    #     instance.Report_To = Report_To
    #     instance.Type = Type
    #     print(instance)
    #     instance.save()
        
    #     print(validated_data)
    #     return instance
    
    
    # def update(self, instance, validated_data):
    #     request = self.context.get('request')
    #     print(request,'requestttttttttttttttt')
    #     # user = User.objects.get(username=instance.user)
    #     instance.user=request.data.get('user', instance.user)
    #     print(instance.user,"------------------")
    #     if user.is_staff:
    #         instance.Mgr_comment = request.data.get('Mgr_comment', instance.Mgr_comment)
    #     elif user.is_superuser:
    #         instance.Mgr_comment = request.data.get('Mgr_comment', instance.Mgr_comment)
    #     elif user.is_superuser and user.is_staff:
    #         instance.Admin_comment = request.data.get('Admin_comment', instance.Admin_comment)
    #     status = request.data.get('Status', instance.Status.status)
    #     instance.Status = StatusAPI.objects.get(status=status)
    #     instance.save()
    #     return instance


# class TicketSerializer(serializers.ModelSerializer):
#     Severity = serializers.CharField(source='Severity.severity', read_only=True)
#     Report_To = serializers.CharField(source='Report_To.manager', read_only=True)
#     Type = serializers.CharField(source='Type.type', read_only=True)
#     Status = serializers.CharField(source='Status.status', read_only=True)
#     ticket_no = serializers.CharField(required=False)
#     user=serializers.CharField()
    
#     class Meta:
#         model = TicketAPI
#         fields = [ 'ticket_no','user', 'Subject', 'Severity', 'Type', 'Report_To', 'Remarks', 'Status', 'Admin_comment',
#                    'Mgr_comment', 'request_raised_at']
        


#     def create(self, validated_data):
#         request = self.context.get('request')
#         user=request.user
#         validated_data['user']=user
#         ticket_no = "OJ-"+uuid.uuid4().hex[:6]
#         validated_data['ticket_no'] = ticket_no
        
#         Severity = request.data.get('Severity')
#         Severity = SeverityAPI.objects.get(severity=Severity)
#         validated_data['Severity'] = Severity

#         Report_To = request.data.get('Report_To')
#         Report_To = ManagerAPI.objects.get(manager=Report_To)
#         validated_data['Report_To'] = Report_To

#         Type = request.data.get('Type')
#         Type = TypeAPI.objects.get(type=Type)
#         validated_data['Type'] = Type

#         instance = self.Meta.model(**validated_data)
#         instance.Severity = Severity
#         instance.Report_To = Report_To
#         instance.Type = Type
#         instance.save()
#         print(instance)
#         return instance
    
    # def update(self, instance, validated_data):
    #     print(validated_data['Admin_comment'], 'validateddataaa')
    #     request = self.context.get('request')
    #     instance.user=request.data.get('user', instance.user)
    #     print(instance.user, 'ins jgjg')
    #     if request.user.is_staff:
    #         instance.Mgr_comment = request.data.get('Mgr_comment', instance.Mgr_comment)
    #     elif request.user.is_superuser:
    #         instance.Mgr_comment = request.data.get('Mgr_comment', instance.Mgr_comment)
    #     elif request.user.is_superuser and request.user.is_staff:
    #         instance.Admin_comment = validated_data['Admin_comment']
    #     status = request.data.get('Status', instance.Status.status)
    #     instance.Status = StatusAPI.objects.get(status=status)
    #     instance.save()
    #     return instance



# class TicketSerializer(serializers.ModelSerializer):
#     Severity = serializers.CharField(source='Severity.severity', read_only=True)
#     Report_To = serializers.CharField(source='Report_To.manager', read_only=True)
#     Type = serializers.CharField(source='Type.type', read_only=True)
#     Status = serializers.CharField(source='Status.status', read_only=True)
#     ticket_no = serializers.CharField(required=False)
    
    
#     class Meta:
#         model = TicketAPI
#         fields = [ 'ticket_no','user', 'Subject', 'Severity', 'Type', 'Report_To', 'Remarks', 'Status', 'Admin_comment',
#                    'Mgr_comment', 'request_raised_at']
        


#     def create(self, validated_data):
#         request = self.context.get('request')
#         user=request.user
#         validated_data['user']=user
#         print(user)
#         ticket_no = "OJ-"+uuid.uuid4().hex[:6]
#         validated_data['ticket_no'] = ticket_no
        
#         Severity = request.data.get('Severity')
#         Severity = SeverityAPI.objects.get(severity=Severity)
#         validated_data['Severity'] = Severity

#         Report_To = request.data.get('Report_To')
#         Report_To = ManagerAPI.objects.get(manager=Report_To)
#         validated_data['Report_To'] = Report_To

#         Type = request.data.get('Type')
#         Type = TypeAPI.objects.get(type=Type)
#         validated_data['Type'] = Type

#         instance = self.Meta.model(**validated_data)
#         instance.Severity = Severity
#         instance.Report_To = Report_To
#         instance.Type = Type
#         instance.save()
#         return instance
    
#     def update(self, instance, validated_data):
        
#         request = self.context.get('request')
#         instance.user=request.data.get('user', instance.user)
        
#         if request.user.is_staff and request.user.is_superuser:
#             instance.Admin_comment = validated_data['Admin_comment']
            
#         elif request.user.is_staff:
#             instance.Mgr_comment = validated_data['Mgr_comment']
            
#         elif request.user.is_staff == False and request.user.is_superuser:
#             instance.Mgr_comment = validated_data['Mgr_comment']
        
#         status = request.data.get('Status', instance.Status.status)
#         instance.Status = StatusAPI.objects.get(status=status)
#         instance.save()
        
#         return instance
            
            
            
##########################################################################################################            
        
class TicketSerializer(serializers.ModelSerializer):
    Severity = serializers.CharField(source='Severity.severity', read_only=True)
    Report_To = serializers.CharField(source='Report_To.manager', read_only=True)
    Type = serializers.CharField(source='Type.type', read_only=True)
    Status = serializers.CharField(source='Status.status', read_only=True)
    ticket_no = serializers.CharField(required=False)
    
    
    class Meta:
        model = TicketAPI
        fields = [ 'id','ticket_no','user', 'Subject', 'Severity', 'Type', 'Report_To', 'Remarks', 'Status', 'Admin_comment',
                   'Mgr_comment', 'request_raised_at']
        

    
    def create(self, validated_data):
        print(validated_data,"validated data")
        
        request = self.context.get('request')
        print(request.user,"request")
        
        user = validated_data['user']
        
        print(validated_data['user'])
        ticket_no = "OJ-"+uuid.uuid4().hex[:6]
        validated_data['ticket_no'] = ticket_no
        
        Severity = request.data.get('Severity')
        Severity = SeverityAPI.objects.get(severity=Severity)
        validated_data['Severity'] = Severity

        Report_To = request.data.get('Report_To')
        Report_To = ManagerAPI.objects.get(manager=Report_To)
        validated_data['Report_To'] = Report_To

        Type = request.data.get('Type')
        Type = TypeAPI.objects.get(type=Type)
        validated_data['Type'] = Type

        instance = self.Meta.model(**validated_data)
        instance.user=user
        instance.Severity = Severity
        instance.Report_To = Report_To
        instance.Type = Type
        instance.save()
        return instance
    
    
    def update(self, instance, validated_data):
        # id=self.Meta.model.objects.get(id=instance.id)
        # print(request.method)
        request = self.context.get('request')
        instance.user=request.data.get('user', instance.user)
        # print(validated_data['Admin_comment'])
        # if request.user.is_staff and request.user.is_superuser:
        # print( validated_data['Admin_comment'],"----------")
        # instance.Admin_comment = validated_data['Admin_comment']
            # print(instance.Admin_comment,"--------------------------------")
        if request.user.is_staff and request.user.is_superuser:
            instance.Admin_comment = validated_data['Admin_comment'] 
        elif request.user.is_staff:
            instance.Mgr_comment = validated_data['Mgr_comment']
            # print( validated_data['Mgr_comment'])
        # print(validated_data['Mgr_comment'])
        # instance.Mgr_comment = validated_data['Mgr_comment']
        # print(instance.Mgr_comment)
            
        # elif request.user.is_staff == False and request.user.is_superuser:
        #     instance.Mgr_comment = validated_data['Mgr_comment']
        
        status = request.data.get('Status', instance.Status.status)
        instance.Status = StatusAPI.objects.get(status=status)
        instance.save()
        
        return instance    
      
   