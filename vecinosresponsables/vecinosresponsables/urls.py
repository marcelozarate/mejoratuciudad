from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^vecinosresponsables/', include('vecinosapp.urls')),
    url(r'^$', 'vecinosapp.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout_then_login', name='logout'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'uploads/(?P<path>.*)',
        'serve', {'document_root': settings.MEDIA_ROOT}),
    )