from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout, password_reset

from django.views.generic import TemplateView
import examplefy.views

# Basics
urlpatterns = patterns('',
    # homepage
    url(r'^$', examplefy.views.homepage, name='homepage'),
    # admin site
    url(r'^admin/', include(admin.site.urls)),
    # viewing an example
    url(r'^example/$',
    TemplateView.as_view(template_name="example.html"),
     name='example')
)

# Authentication
urlpatterns += patterns('',
    url(r'^login/$', login, { 'redirect_field_name': '/' }, name='login'),
    url(r'^logout/$', logout, { 'template_name': 'index.html', 'next_page': '/' }, name='logout'),
    url(r'^password_reset/$', password_reset, name='password_reset'),
)
