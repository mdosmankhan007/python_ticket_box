from django.shortcuts import render
from rest_framework.decorators import api_view
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
# Create your views here.


class SignAPI(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=UsersAPI.objects.all()
    print('outside defdfgdgfdgfd')
    def create(self,request,*args,**kwargs):
            print('hello')
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
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)
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




class LogoutView(APIView):
    def post(self, request):
        logout(request)
        print('yes')
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



class TicketsAPI(viewsets.ModelViewSet):
    serializer_class=TicketSerializer
    queryset=TicketAPI.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]

    
        
    def get_permissions(self):
        if self.request.method == 'PATCH':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


