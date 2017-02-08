from django.shortcuts import render, HttpResponseRedirect, get_object_or_404,Http404
from django.contrib.auth.models import User
from userManagmentApp.forms import MyRegistrationForm, UserCreationForm
from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm
from django.template import loader
from django.template.context_processors import csrf
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# only superuser can reach this page
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    users = User.objects.all()
    user_form = MyRegistrationForm()
    return render(request, 'admin_page.html', {'users': users, 'form': user_form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin_page')

def get_user_form(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = MyRegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404

def create_user(request, user_id = None):
    if request.is_ajax():
        if not user_id:
            user = MyRegistrationForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, isinstance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('inc-users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})
    raise Http404