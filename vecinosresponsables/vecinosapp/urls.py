from django.conf.urls import patterns, url

urlpatterns = patterns('vecinosapp.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^add-aviso/$', 'add_aviso', name='add-aviso'),
    url(r'^list-avisos/$', 'list_avisos', name='list-avisos'),
    url(r'^list-problemas/$', 'list_problemas', name='list-problemas'),
    url(r'^resolver/(?P<aviso_id>\d+)/$', 'resolver', name='resolver'),
)