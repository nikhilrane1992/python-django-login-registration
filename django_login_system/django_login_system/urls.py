from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_login_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', 'django_login_system.views.auth_view'),
    url(r'^login/$', 'django_login_system.views.login'),

#------------------------------------------------------------------------------------------------------------------------
#                             Register New user using django Form
#------------------------------------------------------------------------------------------------------------------------
    url(r'^register_user/$', 'django_login_system.views.register_user'),

#------------------------------------------------------------------------------------------------------------------------
#                             Register new user using post request
#------------------------------------------------------------------------------------------------------------------------
    url(r'^registerUser/$', 'django_login_system.views.registerUser'),


)+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
