from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from bugapp.forms import *
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
def index(request):
    form=User_form()
    if "username" in request.session:

        user = User.objects.get(user_name=request.session['username'])
        return render(request,'index.html',{'form':form,'user':user})
    return render(request,'index.html',{'form':form})

@csrf_exempt
def employee(request):
    if request.method=="POST":
        data={'code':'','msg':''}
        if User.objects.filter(user_name=request.POST.get('username')).count()==0:
            user = User.objects.create(user_name=request.POST.get('username'),password=request.POST.get('password'))
            data['code']=1
            data['msg']='Registered'
            return JsonResponse(data)
        print('coming her')
        data['code']=0
        data['msg']='User Already Exists'
        return JsonResponse(data)
    form=User_form()
    return render(request,'registration.html',{'form':form})

def login(request):
    form=User_form()
    # del request.session['username']
    if not "username" in request.session:
        if request.method=="POST":
            user = User.objects.filter(user_name=request.POST.get('username')).first()
            if user:
                if user.password == request.POST.get('password'):
                    request.session['username'] = user.user_name
                    return redirect(index)
                msg='Invalid password'
                return render(request,'login.html',{'msg':msg,'form':form})
            msg='User does not exists'
            return render(request,'login.html',{'msg':msg,'form':form})
        return render(request,'login.html')
    msg="user logged in already"
    return redirect(index,{'msg':msg,'form':form})

def logout(request):
    form=User_form()
    if "username" in request.session:
        del request.session['username']
        return redirect(index)
    return redirect(index)

def add_project(request):
    if request.method=="POST":
        user = User.objects.get(user_name=request.session['username'])
        project = Project.objects.create(
            project_name = request.POST.get('projectname'),
            project_type = request.POST.get('type'),
            created_by = user
        )
        return redirect(index)
    return render(request,"add_project.html")

def add_bug(request):
    if request.method == "POST":
        user = User.objects.get(user_name=request.session['username'])
        Issue.objects.create(
            project = Project.objects.get(id=request.POST.get('project')),
            issue_name = request.POST.get('issue'),
            issue_descr = request.POST.get('description'),
            assignee = User.objects.get(id=request.POST.get('assignee')),
            status = request.POST.get('status'),
            created_by = user
            )
        return redirect(index)
    projects = Project.objects.all()
    users = User.objects.all()
    return render(request,'add_bug.html',{'projects':projects,'users':users})


def all_projects(request):
    projects = Project.objects.all()
    return render(request,"all_projects.html",{"projects":projects})


def issue_by_user(request,pk=None):
    issues = Issue.objects.filter(assignee=pk)
    print(issues)
    return render(request,'issue_by_user.html',{"issues":issues})


def issue_edit(request,pk=None):
    issue = Issue.objects.filter(id=pk).first()
    user = User.objects.get(user_name=request.session['username'])

    if request.method == "POST":
        print(request.POST)
        issue.issue_name = request.POST.get('issue')
        issue.issue_descr = request.POST.get('description')
        issue.status = request.POST.get('status')
        issue.updated_by = user
        # issue.save()

        print(request)
        # user = User.objects.get(user_name=request.session['username'])
        # Issue.objects.create(
        #     project = Project.objects.get(id=request.POST.get('project')),
        #     issue_name = request.POST.get('issue'),
        #     issue_descr = request.POST.get('description'),
        #     assignee = User.objects.get(id=request.POST.get('assignee')),
        #     status = request.POST.get('status'),
        #     created_by = user
        #     )
        return redirect(index)
    
    print(issue.assignee.user_name)
    return render(request,'issue.html',{'issue':issue,'users':User.objects.all()})
