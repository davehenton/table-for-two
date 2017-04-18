from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from tablefor2 import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': views.home}, name="my_login"),
    url('', include('social_django.urls', namespace='social')),
    # url(r'^register-by-token/(?P<backend>[^/]+)/$', 'register_by_access_token')
]
