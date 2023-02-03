from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
import uuid
import datetime
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
            elif role.role == 'OILC_Manager':
                    user.is_staff=True
                    user.save()
            elif role.role == 'Deployed_Manager':
                    user.is_superuser = True
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
#     Severity = serializers.PrimaryKeyRelatedField(queryset=SeverityAPI.objects.all())
#     Type = serializers.PrimaryKeyRelatedField(queryset=TypeAPI.objects.all())
#     Report_To = serializers.PrimaryKeyRelatedField(queryset=ManagerAPI.objects.all())
#     Status = serializers.PrimaryKeyRelatedField(queryset=StatusAPI.objects.all())
#
# #     Severity = serializers.CharField(source='Severity.severity', read_only=True)
# #     Report_To = serializers.CharField(source='Report_To.manager', read_only=True)
# #     Type = serializers.CharField(source='Type.type', read_only=True)
# #     Status = serializers.CharField(source='Status.status', read_only=True)
# #     ticket_no = serializers.CharField(required=False)
# #
# #     class Meta:
# #         model = TicketAPI
# #         fields = ['ticket_no', 'Subject', 'Severity', 'Type', 'Report_To', 'Remarks', 'Status', 'Admin_comment',
# #                    'Mgr_comment', 'request_raised_at']
# #     def create(self, validated_data):
# #         print("--------------------------------------------------")
# #         print(validated_data,'------------')
# #         ticket_no = "OJ" + uuid.uuid4().hex[:6]
# #         validated_data['ticket_no'] = ticket_no
# #
# #         severity = validated_data.get('Severity', None)
# #         report_to = validated_data.get('Report_To', None)
# #         ticket_type = validated_data.get('Type', None)
# #         status = validated_data.get('Status', None)
# #         # if severity is None or report_to is None or ticket_type is None or status is None:
# #         #     raise serializers.ValidationError("Required fields (Severity, Report_To, Type, Status) are missing")
# #
# #         severity_obj = SeverityAPI.objects.get(severity=severity)
# #         report_to_obj = ManagerAPI.objects.get(manager=report_to)
# #         type_obj = TypeAPI.objects.get(type=ticket_type)
# #         status_obj = StatusAPI.objects.get(status=status)
# #         print(severity_obj,'severity_obj')
# #
# #         validated_data['Severity'] = severity_obj
# #         validated_data['Report_To'] = report_to_obj
# #         validated_data['Type'] = type_obj
# #         validated_data['Status'] = status_obj
# #
# #         return super().create(validated_data)
# #
# #     def update(self, instance, validated_data):
# #
# #         request = self.context.get('request')
# #         user = request.user
# #         print(user, 'user...........')
# #         request = self.context.get('request')
# #         print(request)
# #         status = request.data['Status']
# #         Report_To = request.data['Report_To']
# #         Severity=request.data['Severity']
# #         Type=request.data['Type']
# #         status = StatusAPI.objects.get(status=status)
# #         if user.is_staff:
# #             Mgr_comment=request.data['Mgr_comment']
# #             instance.Mgr_comment = Mgr_comment
# #         elif user.is_superuser:
# #             Admin_comment=request.data['Admin_comment']
# #             instance.Admin_comment = Admin_comment
# #         instance.Status = status
# #         # instance.Report_To = Report_To
# #         instance.Severity = Severity
# #         instance.Type = Type
# #         instance.save()
# #         return instance
#
#
#     class Meta:
#         model = TicketAPI
#         fields = ['ticket_no', 'Subject', 'Severity', 'Type', 'Report_To', 'Remarks', 'Status', 'Admin_comment',
#                    'Mgr_comment', 'request_raised_at']
#
#     # def create(self, validated_data):
#     #     ticket_no = "OJ" + uuid.uuid4().hex[:6]
#     #     validated_data['ticket_no'] = ticket_no
#     #     severity = SeverityAPI.objects.get(severity=self.context.get('severity'))
#     #     validated_data['Severity'] = severity
#     #     type = TypeAPI.objects.get(type=self.context.get('type'))
#     #     validated_data['Type'] = type
#     #     report_to = ManagerAPI.objects.get(manager=self.context.get('report_to'))
#     #     validated_data['Report_To'] = report_to
#     #     status = StatusAPI.objects.get(status=self.context.get('status'))
#     #     validated_data['Status'] = status
#
#         # return super().create(validated_data)
#
#
#     def create(self, validated_data):
#         Severity_id = validated_data.pop('Severity')
#         Type_id = validated_data.pop('Type')
#         Report_To_id = validated_data.pop('Report_To')
#         ticket = TicketAPI.objects.create(
#             Severity=SeverityAPI.objects.get(id=Severity_id),
#             Type=TypeAPI.objects.get(id=Type_id),
#             Report_To=ManagerAPI.objects.get(id=Report_To_id),
#             **validated_data
#         )
#         return ticket
#
#     def update(self, instance, validated_data):
#         request = self.context.get('request')
#         user = request.user
#
#         if user.is_staff:
#             instance.Mgr_comment = request.data.get('Mgr_comment', instance.Mgr_comment)
#         elif user.is_superuser:
#             instance.Admin_comment = request.data.get('Admin_comment', instance.Admin_comment)
#
#         status = request.data.get('Status', instance.Status.status)
#         instance.Status = StatusAPI.objects.get(status=status)
#         instance.save()
#
#         return instance


# class TicketSerializer(serializers.ModelSerializer):
#     Severity = serializers.CharField(source='Severity.severity', read_only=True)
#     Report_To = serializers.CharField(source='Report_To.manager', read_only=True)
#     Type = serializers.CharField(source='Type.type', read_only=True)
#     Status = serializers.CharField(source='Status.status', read_only=True)
#     ticket_no = serializers.CharField(required=False)
#
#     class Meta:
#         model = TicketAPI
#         fields = ['ticket_no', 'Subject', 'Severity', 'Type', 'Report_To', 'Remarks', 'Status', 'Admin_comment',
#                   'Mgr_comment', 'request_raised_at']
#
#     def create(self, validated_data):
#         Severity_name = validated_data.pop('Severity')
#         Type_id = validated_data.pop('Type')
#         Report_To_id = validated_data.pop('Report_To')
#         Status_name = validated_data.pop('Status')
#
#         severity = SeverityAPI.objects.get(name=Severity_name)
#         status = StatusAPI.objects.get(status=Status_name)
#
#         ticket = TicketAPI.objects.create(
#             Severity=severity,
#             Type=TypeAPI.objects.get(id=Type_id),
#             Report_To=ManagerAPI.objects.get(id=Report_To_id),
#             Status=status,
#             **validated_data
#         )
#         return ticket
#
#     def update(self, instance, validated_data):
#         request = self.context.get('request')
#         user = request.user
#         if user.is_staff:
#             instance.Mgr_comment = request.data.get('Mgr_comment', instance.Mgr_comment)
#         elif user.is_superuser:
#             instance.Admin_comment = request.data.get('Admin_comment', instance.Admin_comment)
#         status = request.data.get('Status', instance.Status.status)
#         instance.Status = StatusAPI.objects.get(status=status)
#         instance.save()
#
#         return instance


class TicketSerializer(serializers.ModelSerializer):
    Severity = serializers.CharField(source='Severity.severity', read_only=True)
    Report_To = serializers.CharField(source='Report_To.manager', read_only=True)
    Type = serializers.CharField(source='Type.type', read_only=True)
    Status = serializers.CharField(source='Status.status', read_only=True)
    ticket_no = serializers.CharField(required=False)

    class Meta:
        model = TicketAPI
        fields = ['ticket_no', 'Subject', 'Severity', 'Type', 'Report_To', 'Remarks', 'Status', 'Admin_comment',
                   'Mgr_comment', 'request_raised_at']


    def create(self, validated_data):
        request = self.context.get('request')
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
        instance.Severity = Severity
        instance.Report_To = Report_To
        instance.Type = Type
        instance.save()

        return instance
    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user
        if user.is_staff:
            instance.Mgr_comment = request.data.get('Mgr_comment', instance.Mgr_comment)
        elif user.is_superuser:
            instance.Admin_comment = request.data.get('Admin_comment', instance.Admin_comment)
        status = request.data.get('Status', instance.Status.status)
        instance.Status = StatusAPI.objects.get(status=status)
        instance.save()

        return instance
