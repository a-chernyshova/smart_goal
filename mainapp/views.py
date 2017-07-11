from django.shortcuts import render_to_response,Http404, get_object_or_404
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from userManagmentApp.forms import TasksForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    smart = ['Specific', 'Measurable', 'Achievable', 'Relevant', 'Time bound']
    categorys = Category.objects.all()
    return render(request, "index.html", {'smart': smart, 'categorys':categorys})


@login_required(login_url='/index/')
def category_filter(request):
    if request.method == 'POST':
        category_id = request.POST.get('source')
        if category_id == '0':
            tasks = Tasks.objects.all()
        else:
            tasks = Tasks.objects.filter(category=category_id)
        categorys = Category.objects.all()
        statuses = Status.objects.all()
        return render(request, 'dashboard.html', {'categorys': categorys, 'tasks': tasks, 'statuses': statuses})


@login_required(login_url='/index/')
def state_filter(request):
    if request.method == 'POST':
        state_id = request.POST.get('source')
        print(state_id)
        if state_id == '0':
            tasks = Tasks.objects.all()
        else:
            tasks = Tasks.objects.filter(status=state_id)
        categorys = Category.objects.all()
        statuses = Status.objects.all()
        return render(request, 'dashboard.html', {'categorys': categorys, 'tasks': tasks, 'statuses': statuses})


@login_required(login_url='/index/')
def task(request):
    tasks = Tasks.objects.filter()
    for task in tasks:
        print(task.img.url)
    categorys = Category.objects.all()
    statuses = Status.objects.all()
    paginator = Paginator(tasks, 3)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tasks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tasks = paginator.page(paginator.num_pages)
    return render(request, 'dashboard.html', {'categorys': categorys, 'tasks': tasks, 'statuses': statuses})

@login_required(login_url='/index/')
def category(request, category_id):
    tasks = Tasks.objects.filter(category=category_id)
    categorys = Category.objects.all()
    statuses = Status.objects.all()
    return render(request, 'filter.html', {'categorys': categorys, 'tasks': tasks, 'statuses': statuses})

@login_required(login_url='/index/')
def overview(request):
    tasks = Tasks.objects.all()
    return render(request, 'overview.html', {'tasks':tasks})

@login_required(login_url='/index/')
def create(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create/')
        context = {'form': form}
        return render(request, 'create.html', context)
    context = {'form': TasksForm()}
    return render(request, 'create.html', context)
    #return render(request, 'create.html')

@login_required(login_url='/index/')
def setting(request):
    return render(request, 'settings.html')

@login_required(login_url='/index/')
def detail(request, id):
    task = get_object_or_404(Tasks, id=id)
    comments = Comments.objects.filter(task_id=id)
    subtasks = Sub_tasks.objects.filter(task_id=id)
    return render(request, 'detail.html', {'task': task, 'subtasks': subtasks, 'comments': comments})

@login_required(login_url='/index/')
def subtask_detail(request, id):
    subtask = get_object_or_404(Sub_tasks, id=id)
    return render(request, 'sub_task.html', {'subtask': subtask})

@login_required(login_url='/index/')
def team_work(request):
    return render(request, 'team_work.html')

'''def admin_gems_create(request):
    if request.method == 'POST':
        form = GemsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/gems/')
        context = {'form': form}
        return render(request, 'admin_gems_create.html', context)
    context = {'form': GemsForm()}
    return render(request, 'admin_gems_create.html', context)


def admin_gems_delete(request, id):
    gem = get_object_or_404(Gem, id=id)
    gem.delete()
    return HttpResponseRedirect('/admin/gems/')


def admin_gems_update(request, id):
    gem = get_object_or_404(Gem, id=id)
    if request.method == 'POST':
        # form = GemsForm(request.POST or None, instance=gem)
        form = GemsForm(request.POST, instance=gem)
        if form.is_valid():
            gem.save()
            return HttpResponseRedirect('/admin/gems/')
        context = {'form': form}
        return render(request, 'admin_gems_update.html', context)
    context = {'form': GemsForm(instance=gem)}
    return render(request, 'admin_gems_update.html', context)'''