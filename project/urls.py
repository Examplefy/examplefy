from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import examplefy.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', examplefy.views.homepage, name='homepage'),
    url(r'^db', examplefy.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
