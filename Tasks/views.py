from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Task
import bcrypt

# CREATE 
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            print(errors)
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register')
        else:
            email = request.POST['email'].lower()
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash)
            created_user = User.objects.create(first_name = request.POST['first_name'], email = email, password = pw_hash)
            request.session['user_id'] = created_user.id
            created_user.save()
            print(created_user)
            return redirect('/homepage')

def new_task(request):
    if request.method == 'GET':
        return render(request, 'new_task.html')
    if request.method == 'POST':
        this_user = User.objects.get(id = request.session['user_id'])
        created_task = Task.objects.create(title = request.POST['title'], description = request.POST['description'], priority = request.POST['priority'], user = this_user)
        created_task.save()
        print(created_task)
        return redirect('/homepage')


# READ
def index(request):
    return render(request, 'index.html')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        print(logged_user)
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
        return redirect('/homepage')
    return redirect('/')

def homepage(request):
    this_user = User.objects.get(id = request.session['user_id'])
    context = {
        'first_name':  this_user.first_name,
        'tasks': this_user.tasks.all(),
    }
    return render(request, 'homepage.html', context)

def filter_tasks_by_priority(request):
    this_user = User.objects.get(id = request.session['user_id'])
    context ={
        'first_name': this_user.first_name,
        'filtered_tasks': this_user.tasks.all().order_by('priority'),
    }
    return render(request, 'filtered_homepage.html',  context)


# UPDATING
def edit_task(request, id):
    if request.method == 'GET':
        this_task = Task.objects.get(id = id)
        context = {
            'task_id': this_task.id,
            'title': this_task.title,
            'priority': this_task.priority,
            'description': this_task.description,
        }
        return render(request, 'edit_task.html', context)
    if request.method == 'POST':
        this_task =  Task.objects.get(id = id)
        this_task.title = request.POST['title']
        this_task.priority = request.POST['priority']
        this_task.description = request.POST['description']
        this_task.save()
        return redirect('/homepage')


# DELETE
def logout(request):
    request.session.flush()
    return redirect('/')

def delete_task(request, id):
    this_task = Task.objects.get(id = id)
    this_task.delete()
    return redirect('/homepage')

# Create your views here.
