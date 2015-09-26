from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'Principal.views.home', name='home'),
    url(r'^contact/$', 'Principal.views.contact', name='contact'),
    url(r'^blog/$', 'Principal.views.blog', name='blog'),
	url(r'^about/$', 'Principal.views.about', name='about'), 
	url(r'^linen_index/$', 'Principal.views.linenIndex', name='linenIndex'),
	##############	Linen's Detail	##############
	url(r'^fortuny_detail/$', 'Principal.views.fortunyDetail', name='fortunyDetail'),
	url(r'^galaxy_detail/$', 'Principal.views.galaxyDetail', name='galaxyDetail'),
	url(r'^novelty_detail/(?P<page>\d+)?', 'Principal.views.noveltyDetail', name='noveltyDetail'),
	url(r'^organza_detail/$', 'Principal.views.organzaDetail', name='organzaDetail'),
	url(r'^pintuck_detail/$', 'Principal.views.pintuckDetail', name='pintuckDetail'),
	url(r'^satin_detail/$', 'Principal.views.satinDetail', name='satinDetail'),
	url(r'^chevron_detail/$', 'Principal.views.chevronDetail', name='chevronDetail'),
	url(r'^chair_index/$', 'Principal.views.chairIndex', name='chairIndex'),
	url(r'^service_laundry$', 'Principal.views.serviceLaundry', name='serviceLaundry'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
