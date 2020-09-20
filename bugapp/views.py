from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from bugapp.forms import *
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
    form=User_form()
    if "username" in request.session:
        user = User.objects.get(user_name=request.session['username'])
        closed_issues = Issue.objects.filter(assignee_id = user.id,status="Closed").count()
        all_issues = Issue.objects.filter(assignee_id = user.id).count()
        open_issues = all_issues - closed_issues
        all_reported = Issue.objects.filter(created_by_id = user.id).count()
        closed_issues_reported = Issue.objects.filter(created_by_id = user.id,status="Closed").count()
        open_issues_reported = all_reported - closed_issues_reported
        return render(request,'issues_count_list.html',{'form':form,'user':user,'closed_issues':closed_issues,
            'open_issues':open_issues,'all_issues':all_issues,
            'all_reported':all_reported,'closed_issues_reported':closed_issues_reported,'open_issues_reported':open_issues_reported})
    return render(request,'index.html',{'form':form})

def issue_stats(request,status):
    user = User.objects.get(user_name=request.session['username'])

    if status == "Closed":
        issues = Issue.objects.filter(assignee_id = user.id,status="Closed")
    elif status == "Open":
        issues = Issue.objects.filter(assignee_id = user.id).exclude(status="Closed")
    elif status == 'All':
        issues = Issue.objects.filter(assignee_id = user.id)

    elif status == "Closed_reported":
        issues = Issue.objects.filter(created_by_id = user.id,status="Closed")
    elif status == "Open_reported":
        issues = Issue.objects.filter(created_by_id = user.id).exclude(status="Closed")
    elif status == "All_reported":
        issues = Issue.objects.filter(created_by_id = user.id)

    return render(request,'issue_by_user.html',{"issues":issues})



@csrf_exempt
def employee(request):
    if request.method=="POST":
        data={'code':'','msg':''}
        if User.objects.filter(user_name=request.POST.get('username')).count()==0:
            user = User.objects.create(user_name=request.POST.get('username'),password=request.POST.get('password'))
            data['code']=1
            data['msg']='Registered'
            return JsonResponse(data)
        data['code']=0
        data['msg']='User Already Exists'
        return JsonResponse(data)
    form=User_form()
    return render(request,'registration.html',{'form':form})

def login(request):
    form=User_form()
    if request.session._session:
        del request.session
    if request.method == "POST":
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

def logout(request):
    if "username" in request.session:
        del request.session["username"]
        return redirect(index)
    return redirect(index)

def add_project(request):
    user = User.objects.get(user_name=request.session['username'])
    if request.method=="POST":
        project = Project.objects.create(
            project_name = request.POST.get('projectname'),
            project_type = request.POST.get('type'),
            created_by = user
        )
        return redirect(index)
    return render(request,"add_project.html",{"user":user})

def add_bug(request):
    if request.method == "POST":
        user = User.objects.get(user_name=request.session['username'])
        Issue.objects.create(
            project_id = request.POST.get('project'),
            issue_name = request.POST.get('issue'),
            issue_descr = request.POST.get('description'),
            assignee_id = request.POST.get('assignee'),
            status = request.POST.get('status'),
            created_by_id = user.id
            )
        return redirect(index)
    projects = Project.objects.filter(Q())
    users = User.objects.filter(Q())
    return render(request,'add_bug.html',{'projects':projects,'users':users})


def all_projects(request):
    projects = Project.objects.all()
    return render(request,"all_projects.html",{"projects":projects})


def issue_by_user(request,pk=None):
    issues = Issue.objects.filter(assignee=pk)
    return render(request,'issue_by_user.html',{"issues":issues})


def issue_edit(request,pk=None):
    query=Q()
    issue = Issue.objects.filter(id=pk).first()
    if request.method == "POST":
        user = User.objects.get(user_name=request.session['username'])
        issue.issue_name = request.POST.get('issue')
        issue.issue_descr = request.POST.get('description')
        issue.status = request.POST.get('status')
        issue.assignee_id = request.POST.get('assignee')
        issue.updated_by_id = user.id
        issue.save()
        return redirect(issue_edit,issue.id)
    return render(request,'issue.html',{'issue':issue,'users':User.objects.filter(query)})