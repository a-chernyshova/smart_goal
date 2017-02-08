from django.shortcuts import render_to_response,Http404, get_object_or_404
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from userManagmentApp.forms import TasksForm
from django.contrib.auth.decorators import login_required

def index(request):
    smart = ['Specific', 'Measurable', 'Achievable', 'Relevant', 'Time bound']
    categorys = Category.objects.all()
    return render(request, "index.html", {'smart': smart, 'categorys':categorys})

@login_required(login_url='/index/')
def task(request):
    tasks = Tasks.objects.filter()
    categorys = Category.objects.all()
    return render(request, 'dashboard.html', {'categorys':categorys, 'tasks':tasks})

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
def settings(request):
    return render(request, 'settings.html')

@login_required(login_url='/index/')
def team_work(request):
    return render(request, 'team_work.html')
'''
def task_detail(request, id):
    task = get_object_or_404(Tasks, id=id)
    return render(request, 'task_detail.html', {'task':task})'''

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
    return render(request, 'admin_gems_update.html', context)'''''