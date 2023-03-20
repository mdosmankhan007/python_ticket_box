"""ticketproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ticketapp import views
from ticketapp import views_old
from ticketapp.views import LoginAPI
from ticketapp.serializers import *

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
router=routers.DefaultRouter()
router.register('signup',views.SignAPI)
router.register('role',views.RolesAPI)
router.register('severity',views.SeveritysAPI)
router.register('status',views.StatussAPI)
router.register('manager',views.ManagersAPI)
router.register('type',views.TypesAPI)
router.register('ticket',views.TicketsAPI)
router.register('empticket',views.EmployeeDetail,basename="Employee")
router.register('admincomment',views.AdminComment)
router.register('managercomment',views.ManagerComment)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/login/',LoginAPI.as_view(actions={'post': 'post'})),
    
    path('api/tickets/<int:id>/', views.TicketsAPI.as_view({'patch': 'update'})),
    # path('api/login/',LoginAPI.as_view()),
    path('api/logout/', views.LogoutView.as_view()),

    path("", views_old.home, name="homepage"),

    path("employee", views_old.employee, name='employee'),
    # path("manager",views.manager,name='manager'),
    path("manager", views_old.reporting1, name='manager'),
    # path("reporting1", views.reporting1, name='reporting1'),
    # path("reporting2", views_old.reporting2, name='reporting2'),
    path("adminpage", views_old.admin, name='admin'),
    path('login/', views_old.user_login, name="logpage"),

    #
    path('sign/', views_old.signup, name="signup"),
    path('logout/', views_old.ulogout, name="logout"),
    path('accept/<int:model>/<int:id>', views_old.accept, name='accept'),
    path('reject/<int:model>/<int:id>', views_old.reject, name='reject'),
    path('complete/<int:model>/<int:id>', views_old.complete, name='complete'),

    path('comment/<int:model>/<int:id>', views_old.comment, name='comment'),
    path('Mcomment/<int:model>/<int:id>', views_old.Mgrcomment, name='Mgrcomment'),
    path('ticket/', views_old.ticket, name='ticket'),
    path('t_id/<int:model>/<int:id>/<str:ticket_no>/', views_old.ticket_id, name='ticket_id')

]

