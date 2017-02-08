"""smart_goal URL Configuration
Examples:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainapp.views import *
from userManagmentApp.views import *
from adminApp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^index', index),
    url(r'^registration', registration)
]

urlpatterns += [
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout),
    url(r'^user/registration/$', registration),
    url(r'^admin_page/$', admin_page),
    url(r'^dashboard/$', task),
    url(r'^overview/$', overview),
    url(r'^create/$', create),
    url(r'^settings/$', settings),
    url(r'^team_work/$', team_work),
    url(r'^admin_page/delete/user/(\d+)$', delete_user),
    url(r'^admin_page/get_user_form/(\d+)$', get_user_form),
    url(r'^admin_page/create/user/(\d*)$', create_user),
]