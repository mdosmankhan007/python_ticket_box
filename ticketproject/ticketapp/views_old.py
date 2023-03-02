from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
import uuid


# Create your views here.

def home(request):
    return render(request, 'home.html')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                obj=Pusers.objects.filter(username=username).values()
                if user is not None:
                    if obj[0]['role']=='admin':
                        login(request, user)
                        return HttpResponseRedirect('/adminpage')
                    elif obj[0]['role']=='OILC_Manager':
                        login(request, user)
                        return HttpResponseRedirect('/manager')
                    elif obj[0]['role'] == 'Deployed_Manager':
                        login(request, user)
                        return HttpResponseRedirect('/reporting2')
                    else:
                        login(request, user)
                        return HttpResponseRedirect('/employee')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/sign')


def signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            first_name = fm.cleaned_data['first_name']
            last_name = fm.cleaned_data['last_name']
            email = fm.cleaned_data['email']
            role = fm.cleaned_data['role']
            password = fm.cleaned_data['password2']
            puser = Pusers.objects.create(username=username, first_name=first_name, last_name=last_name, email=email,
                                          password=password, role=role)
            user1 = User.objects.create_user(username=username, password=password, email=email)
            puser.save()
            if role == 'OILC_Manager' or role == 'Deployed_Manager':
                user1.is_staff = True
                user1.save()
            elif role == 'admin':
                user1.is_superuser = True
                user1.save()
            else:
                user1.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def reporting1(request):
    obj = Ticket.objects.all()
    return render(request, 'manager.html', {'obj': obj})


# def reporting2(request):
#     obj = Ticket.objects.all()
#     print(obj)
#     return render(request, 'Manager2.html', {'obj': obj})


def ulogout(request):
    logout(request)
    return HttpResponseRedirect('/login')



def employee(request):
    id = 'raised'
    ticketmodel = Ticket.objects.all()
    context = { 'id': id, 'ticket': ticketmodel}
    return render(request, 'employee.html', context)

def admin(request):
    id = 'raised'
    ticket = Ticket.objects.all()
    context = {'ticket': ticket}
    return render(request, 'admin.html', context)




def accept(request, model, id):
    if model == 5:
        tmodel = Ticket.objects.get(id=id)
        tmodel.Status = 'accepted'
        tmodel.save(update_fields=['Status'])

    return HttpResponseRedirect('/manager')


def comment(request, model, id):
    if model == 5:
        tmodel = Ticket.objects.get(id=id)
        fm = Comment(request.POST, instance=tmodel)
        if request.method == 'POST':
            # fm=Ticket(request.POST,instance=tmodel)
            if fm.is_valid():
                fm.save()
            return HttpResponseRedirect('/adminpage')
        else:
            return render(request, 'edit.html', {'form': fm})


def Mgrcomment(request, model, id):
    if model == 5:
        tmodel = Ticket.objects.get(id=id)
        fm = Mngr_comment(request.POST, instance=tmodel)
        if request.method == 'POST':
            # fm=Ticket(request.POST,instance=tmodel)
            if fm.is_valid():
                fm.save()
            return HttpResponseRedirect('/manager')
        else:
            return render(request, 'Accept_Reject.html', {'form': fm})


def reject(request, model, id):
    if model == 5:
        tmodel = Ticket.objects.get(id=id)
        tmodel.Status = 'rejected'
        tmodel.save(update_fields=['Status'])
    return HttpResponseRedirect('/manager')


def complete(request, model, id):
    if model == 5:
        smodel = Ticket.objects.get(id=id)
        smodel.Status = 'completed'
        smodel.save(update_fields=['Status'])
    return HttpResponseRedirect('/adminpage')


def ticket(request):
    ticket = uuid.uuid4().hex
    ticket1 = ticket[:6]
    if request.method == 'POST':
        fm = TicketForm(data=request.POST)

        if fm.is_valid():
            print(fm.cleaned_data)
            Ticket_data = Ticket.objects.create(user=request.user, Subject=request.POST.get('Subject'),
                                                ticket_no='OJ-' + ticket1,
                                                Severity=request.POST.get('Severity'),
                                                Type=request.POST.get('Type'),
                                                Report_To=request.POST.get('Report_To'),
                                                Remarks=request.POST.get('Remarks'))
            Ticket_data.save()
        return HttpResponseRedirect('/employee')
    else:
        fm = TicketForm()
    return render(request, 'ticket.html', {'form': fm})


def ticket_id(request, model, id, ticket_no):
    if model == 5:
        b = Ticket.objects.get(ticket_no=ticket_no)
        return render(request, 'ticket_info.html', {'b': b})




