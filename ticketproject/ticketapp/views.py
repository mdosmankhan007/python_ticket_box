from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator
# Create your views here.


class SignAPI(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=UsersAPI.objects.all()
    def create(self,request,*args,**kwargs):
            model1=UserSerializer(data=request.data, context={'request': request})
            # role = request.data.get('role')
            # role = RoleAPI.objects.get(role=role)
            model1.is_valid(raise_exception=True)
            # model1.role = role
            model1.save()
            print(model1.data, "---")
            return Response(model1.data)


        

class LoginAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            
            user = User.objects.get(username=username)
            print(user)
            if user.is_authenticated:
                user1 = UsersAPI.objects.filter(username=username).first()
                if user is not None:
                    if user.check_password(password):
                            login(request, user)
                            return Response({
                                'status': 'success',
                                'data': username,
                                'is_superuser': user.is_superuser,
                                'is_staff': user.is_staff,
                                'role': user1.role.role,
                                'message': f'login successful {username}'
                            })
                    else:
                        raise AuthenticationFailed('password not match')
                else:
                    raise AuthenticationFailed('user not found')
            else:
                raise AuthenticationFailed('check username and password')
        except:
            return Response({"provide correct username and password"})




class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response('logged out succefully')




class RolesAPI(viewsets.ModelViewSet):
    serializer_class=RoleAPISerializer
    queryset=RoleAPI.objects.all()



class SeveritysAPI(viewsets.ModelViewSet):
    serializer_class=SeverityAPISerializer
    queryset=SeverityAPI.objects.all()

class StatussAPI(viewsets.ModelViewSet):
    serializer_class=StatusAPISerializer
    queryset=StatusAPI.objects.all()

class TypesAPI(viewsets.ModelViewSet):
    serializer_class=TypeAPISerializer
    queryset=TypeAPI.objects.all()

class ManagersAPI(viewsets.ModelViewSet):
    serializer_class=ManagerAPISerializer
    queryset=ManagerAPI.objects.all()



# class TicketsAPI(viewsets.ModelViewSet):
#     serializer_class=TicketSerializer
#     queryset=TicketAPI.objects.all()
#     authentication_classes = [SessionAuthentication]
#     # permission_classes = [IsAuthenticated]
   
#     def get_permissions(self):
#         if self.request.method == 'PATCH':
#             self.permission_classes = [IsAdminUser]
#         return super().get_permissions()


# from rest_framework import permissions

# class IsAuthenticatedAndStaff(permissions.BasePermission):
#     def has_permission(self, request, view):
#         print(request.user, '----------')
#         return request.user.is_staff and request.user.is_superuser == False
    
# class IsAuthenticatedAndStaff1(permissions.BasePermission):
#     def has_permission(self, request, view):
#         print(request.user, '----------')
#         return request.user.is_staff == False and request.user.is_superuser == True
    
# class IsAuthenticatedAndStaff2(permissions.BasePermission):
#     def has_permission(self, request, view):
#         print(request.user, '----------')
#         return request.user.is_staff == True and request.user.is_superuser == True

@method_decorator(csrf_exempt, name='dispatch')
class TicketsAPI(viewsets.ModelViewSet):
    serializer_class=TicketSerializer
    queryset=TicketAPI.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    
    def get_permissions(self):
        if self.request.method == 'PATCH':
            self.permission_classes = [permission for permission in self.permission_classes if permission != IsAuthenticated or permission != AllowAny]
        return super().get_permissions()
    
    # def create(self, validated_data):
    #     print(validated_data,"validated data")
    #     # print(validated_data['username'],"validated data userrrrrr")
    #     request = self.context.get('request')
    #     print(request.user,"request")
    #     # user=request.user.username
    #     # print(validated_data['user'],"usernameeeeeeeeeeeeeeeee")
    #     user = validated_data['user']
    #     # validated_data['user'] = user
    #     print(validated_data['user'])
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

    #     instance = self.Meta.model(**validated_data)
    #     instance.user=user
    #     print(instance.user,"-----------")
    #     instance.Severity = Severity
    #     instance.Report_To = Report_To
    #     instance.Type = Type
    #     instance.save()
    #     return instance
    
    
    # def update(self, instance, validated_data):
        
    #     request = self.context.get('request')
    #     instance.user=request.data.get('user', instance.user)
    #     print(instance.id)
    #     if request.user.is_staff and request.user.is_superuser:
    #         instance.Admin_comment = validated_data['Admin_comment']
            
    #     elif request.user.is_staff:
    #         instance.Mgr_comment = validated_data['Mgr_comment']
            
    #     elif request.user.is_staff == False and request.user.is_superuser:
    #         instance.Mgr_comment = validated_data['Mgr_comment']
        
    #     status = request.data.get('Status', instance.Status.status)
    #     instance.Status = StatusAPI.objects.get(status=status)
    #     instance.save()
        
    #     return instance    